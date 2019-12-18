#  File: ConvexHull.py

#  Description: Takes pairs of points and computes the area of the smallest
#               convex polygon containing all points

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/25/19

#  Date Last Modified: 9/25/19

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# compute and return the determinant of the coordinates of three points
# p, q, and r are Point objects
def det (p, q, r):
  return q.x * r.y + p.x * q.y + p.y * r.x - q.y * r.x - p.x * r.y - p.y * q.x

# computes and returns the convex hull of a sorted list of Points
# convex hull is a list of Point objects starting at the extreme
# left point and going clockwise in order
def convex_hull (sorted_points):
  upper_hull = []
  upper_hull.append(sorted_points[0])
  upper_hull.append(sorted_points[1])
  for i in range(2, len(sorted_points)):
    upper_hull.append(sorted_points[i])
    while (len(upper_hull) >= 3 
            and det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) > 0):
      upper_hull.pop(-2)
  
  lower_hull = []
  lower_hull.append(sorted_points[-1])
  lower_hull.append(sorted_points[-2])
  for i in range(len(sorted_points) - 3, -1, -1):
    lower_hull.append(sorted_points[i])
    while (len(lower_hull) >= 3 and
            det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) > 0):
      lower_hull.pop(-2)
  
  lower_hull.pop(-1)  # pops last point
  lower_hull.pop(0)   # pops first point
  convex_hull = upper_hull
  convex_hull.extend(lower_hull)
  return convex_hull

# compute and return the area of a convex polygon
# convex_poly is a list of Point objects that define the vertices
# of a convex polygon in order
def area_poly (convex_poly):
  area = 0
  area += (convex_poly[-1].x * convex_poly[0].y 
            - convex_poly[-1].y * convex_poly[0].x)
  for i in range(len(convex_poly) - 1):
    area += (convex_poly[i].x * convex_poly[i+1].y 
            - convex_poly[i].y * convex_poly[i+1].x)
  return 0.5 * abs(area)

# returns x and y coordinates as a tuple for sorting list of points
def sort_points(point):
  return point.x, point.y

def main():
  # create an empty list of Point objects
  point_list = []

  # open file points.txt for reading
  with open("points.txt", 'r') as inFile:
    # read file line by line, create Point objects and store in file
    num_of_points = int(inFile.readline())
    for i in range(num_of_points):
      point = tuple(map(int, inFile.readline().strip().split()))
      point_list.append(Point(point[0], point[1]))
    
  # sort the list according to x-coordinates
  sorted_point_list = sorted(point_list, key=sort_points)
  
  # get the convex hull
  polygon_verticies = convex_hull(sorted_point_list)

  # print the convex hull
  print("Convex Hull")
  for vertex in polygon_verticies:
    print(vertex)

  # get the area of the convex hull
  area = area_poly(polygon_verticies)

  # print the area of the convex hull
  print("\nArea of Convex Hull =", area)

# YOU MUST WRITE THIS LINE AS IS
if __name__ == "__main__":
  main()
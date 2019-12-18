#  File: Geom.py

#  Description: Has class definitions for Point, Circle, and Rectangle classes.
#               main() test the three classes

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/18/19

#  Date Last Modified: 9/19/19

import math

class Point (object):
  # constructor 
  # x and y are floats
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  # other is a Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  # takes no arguments
  # returns a string
  def __str__ (self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  # x, y, and radius are floats
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c overlaps this circle (non-zero area of overlap)
  # but neither is completely inside the other
  # the only argument c is a Circle object
  # returns a boolean
  def circle_overlap (self, c):
    # define bigger and smaller circle
    if self.radius > c.radius:
      bigger_circle = self
      smaller_circle = c
    else:
      bigger_circle = c
      smaller_circle = self
    # c center is inside self center
    if bigger_circle.point_inside(smaller_circle.center):
      if bigger_circle.center.dist(smaller_circle.center) + smaller_circle.radius > \
         bigger_circle.radius:
        return True
    elif bigger_circle.center.dist(smaller_circle.center) < bigger_circle.radius + smaller_circle.radius:
      return True
    return False
   
  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  # the only argument, r, is a rectangle object
  def circle_circumscribe (self, r):
    # find rectangle center
    length = r.length()
    width = r.width()
    center = Point(r.ul.x + length / 2, r.ul.y - width / 2)
	# find radius of circle
    radius = center.dist(r.ul)
    return Circle(radius, center.x, center.y)

  # string representation of a circle
  # takes no arguments and returns a string
  def __str__ (self):
    return "Radius: " + str(self.radius) + ", Center: " + str(self.center)
    
  # test for equality of radius
  # the only argument, other, is a circle
  # returns a boolean
  def __eq__ (self, other):
    tol = 1.0e-8
    if abs(self.radius - other.radius) < tol:
      return True
    return False

class Rectangle (object):
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
  # takes no arguments, returns a float
  def length (self):
    return self.lr.x - self.ul.x

  # determine width of Rectangle (distance along the y axis)
  # takes no arguments, returns a float
  def width (self):
    return self.ul.y - self.lr.y

  # determine the perimeter
  # takes no arguments, returns a float
  def perimeter (self):
    return (self.length() + self.width()) * 2
    
  # determine the area
  # takes no arguments, returns a float
  def area (self):
    return self.length() * self.width()

  # determine if a point is strictly inside the Rectangle
  # takes a point object p as an argument, returns a boolean
  def point_inside (self, p):
    if self.ul.x < p.x < self.lr.x and self.lr.y < p.y < self.ul.y:
      return True
    return False

  # determine if another Rectangle is strictly inside this Rectangle
  # takes a rectangle object r as an argument, returns a boolean
  # should return False if self and r are equal
  def rectangle_inside (self, r):
    if self.ul.x < r.ul.x and self.ul.y > r.ul.y and self.lr.x > r.lr.x and self.lr.y < r.lr.y:
      return True
    return False

  # determine if two Rectangles overlap (non-zero area of overlap)
  # takes a rectangle object r as an argument returns a boolean
  def rectangle_overlap (self, r):
	# if any corner is in rectangle
    if check_vertices(self, r) or check_vertices(r, self):
      return True
    elif check_edges(self, r) or check_edges(r, self):
      return True
    return False

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  # takes a circle object c as input and returns a rectangle object
  def rectangle_circumscribe (self, c):
	# find radius of circle
    ul_x = c.center.x - c.radius
    ul_y = c.center.y + c.radius
    lr_x = c.center.x + c.radius
    lr_y = c.center.y - c.radius
    return Rectangle(ul_x, ul_y, lr_x, lr_y)

  # give string representation of a rectangle
  # takes no arguments, returns a string
  def __str__ (self):
    return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

  # determine if two rectangles have the same length and width
  # takes a rectangle other as argument and returns a boolean
  def __eq__ (self, other):
    tol = 1e-8
    if abs(self.width() - other.width()) < tol and abs(self.length() - other.length()) < tol:
      return True
    return False

# determines if any vertices of one rectangle but not all are inside another rectangle
def check_vertices(r1, r2):
  if r1.point_inside(r2.ul) or r1.point_inside(Point(r2.ul.x, r2.lr.y)) or \
    r1.point_inside(r2.lr) or r1.point_inside(Point(r2.lr.x, r2.ul.y)):
    if r1.point_inside(r2.ul) and r1.point_inside(Point(r2.ul.x, r2.lr.y)) and \
      r1.point_inside(r2.lr) and r1.point_inside(Point(r2.lr.x, r2.ul.y)):
        return False
    return True
  return False

# checks two rectangles to see if the edges intersect
def check_edges(r1, r2):
  if r1.ul.x < r2.ul.x and r1.lr.x > r2.lr.x:
    if r1.ul.y < r2.ul.y and r1.lr.y > r2.lr.y:
      return True
  return False

def main():
  # open the file geom.txt
  with open("geom.txt", 'r') as inFile:
    # create Point objects P and Q
    keys_names = ['P', 'Q', 'C', 'D', 'G', 'H']
    geo_dict = {}
    for line in range(6):
      read_line = inFile.readline().split('#')
      geo_dict[keys_names[line]] = list(map(float, read_line[0].strip().split()))

  # print the coordinates of the points P and Q
  p = Point(geo_dict['P'][0], geo_dict['P'][1])
  q = Point(geo_dict['Q'][0], geo_dict['Q'][1]) 
  print("Coordinates of P:", p)
  print("Coordinates of Q:", q)

  # find the distance between the points P and Q
  print("Distance between P and Q:", p.dist(q))

  # create two Circle objects C and D
  c = Circle(geo_dict['C'][0], geo_dict['C'][1], geo_dict['C'][2])
  d = Circle(geo_dict['D'][0], geo_dict['D'][1], geo_dict['D'][2])

  # print C and D
  print("Circle C:", c)
  print("Circle D:", d)

  # compute the circumference of C
  print("Circumference of C:", c.circumference())

  # compute the area of D
  print("Area of D:", d.area())

  # determine if P is strictly inside C
  print("P {} inside C".format("is" if c.point_inside(p) else "is not"))

  # determine if C is strictly inside D
  print("C {} inside D".format("is" if d.circle_inside(c) else "is not"))

  # determine if C and D intersect (non zero area of intersection)
  print("C {} intersect D".format("does" if c.circle_overlap(d) else "does not"))

  # determine if C and D are equal (have the same radius)
  print("C {} equal to D".format("is" if c == d else "is not"))

  # create two rectangle objects G and H
  g = Rectangle(geo_dict['G'][0], geo_dict['G'][1], geo_dict['G'][2], geo_dict['G'][3])
  h = Rectangle(geo_dict['H'][0], geo_dict['H'][1], geo_dict['H'][2], geo_dict['H'][3])
  
  # print the two rectangles G and H
  print("Rectangle G:", g)
  print("Rectangle H:", h)

  # determine the length of G (distance along x axis)
  print("Length of G:", g.length())

  # determine the width of H (distance along y axis)
  print("Width of H:", h.width())

  # determine the perimeter of G
  print("Perimeter of G:", g.perimeter())

  # determine the area of H
  print("Area of H:", h.area())

  # determine if point P is strictly inside rectangle G
  print("P {} inside G".format("is" if g.point_inside(p) else "is not"))

  # determine if rectangle G is strictly inside rectangle H
  print("G {} inside H".format("is" if h.rectangle_inside(g) else "is not"))

  # determine if rectangles G and H overlap (non-zero area of overlap)
  print("G {} overlap H".format("does" if h.rectangle_overlap(g) else "does not"))

  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
  print("Circle that circumscribes G:", c.circle_circumscribe(g))

  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle
  print("Rectangle that circumscribes D:", g.rectangle_circumscribe(d))

  # determine if the two rectangles have the same length and width
  print("Rectangle G {} equal to H".format("is" if g == h else "is not"))

  # close the file geom.txt
  inFile.close()

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()

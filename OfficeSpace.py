#  File: OfficeSpace.py

#  Description: Program takes employee requests for cubicle space
#               within an office; determines total office space,
#               office space unclaimed, and uncontested space for 
#               for each employee. Can handle multiple office 
#               datasets at a time.

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/20/19

#  Date Last Modified: 9/20/19

class Point():
    # constructor
    # x and y are floats
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y
class Rectangle():
    # constructor
    def __init__ (self, ll_x = 0, ll_y = 1, ur_x = 1, ur_y = 0):
        if ((ll_x < ur_x) and (ll_y < ur_y)):
            self.ll = Point (ll_x, ll_y)
            self.ur = Point (ur_x, ur_y)
        else:
            self.ll = Point (0, 1)
            self.ur = Point (1, 0)
    def point_inside(self, p):
        if self.ll.x < p.x < self.ur.x and self.ll.y < p.y < self.ur.y:
            return True
        return False
class Office():
    def __init__(self,gridDim,numEmploy,requestDict):
        self.gridDim = gridDim
        self.numEmploy = numEmploy
        self.requestDict = requestDict
        self.totalArea = self.total_area()
        self.grid = self.matrix_init()
        self.unallocated = 0 #total area that no employee has requested
        self.contested = 0 #total area that is contested
        self.employDict = self.employ_dict_init() #employee names are keys and guaranteed office space are values
        self.sweep_grid() #method that sweeps office grid and updates unallocated, contested, and employDict attributes
    def employ_dict_init(self):
        employDict = {}
        for key in self.requestDict:
            employDict[key] = 0
        return employDict
    def total_area(self):
        return self.gridDim[0]*self.gridDim[1]
    def matrix_init(self): #creates a NxM array of empty lists
        matrix = []
        for i in range(self.gridDim[0]):
            row = []
            for j in range(self.gridDim[1]):
                row.append([])
            matrix.append(row)
        return matrix
    def sweep_grid(self):
        for i in range(self.gridDim[0]):
            for j in range(self.gridDim[1]):
                point = Point(i+0.5, j+0.5) #sample point is the center point of the scanned grid square
                for key in self.requestDict: #searches through all employees request rectangles
                    if self.requestDict[key].point_inside(point): #sees if sample point is within rectangle
                        self.grid[i][j].append(key)
                if len(self.grid[i][j]) == 0: #no employee has requested the square
                    self.unallocated += 1
                elif len(self.grid[i][j]) == 1: #only one employee has requested the square
                    self.employDict[self.grid[i][j][0]] += 1
                else: #more than one employee has requested the square
                    self.contested += 1
    def __str__(self):
        output = 'Total {0}\nUnallocated {1}\nContested {2}\n'.format(self.totalArea, self.unallocated, self.contested)
        for key in self.employDict:
            output += '{} {}\n'.format(key,self.employDict[key])
        return output
def main():
    with open('office.txt','r') as fileOpen:
        officeList = [] #list of datasets for each office
        gridDim = list(map(int, fileOpen.readline().strip().split()))
        while True:
            numEmploy = int(fileOpen.readline().strip())
            requestDict = {} #dictionary of employee and their office space requested expressed as a rectangle
            for i in range(numEmploy):
                line = fileOpen.readline().strip().split()
                line[1:] = list(map(int,line[1:]))
                requestDict[line[0]] = Rectangle(line[1],line[2],line[3],line[4])
            officeList.append(Office(gridDim, numEmploy, requestDict))
            line = fileOpen.readline().strip().split()
            if line == []:
                break
            else:
                gridDim = list(map(int, line))
    for office in officeList:
        print(office) #prints necessary data for each office
main()




#  File: Triangle.py

#  Description: Finds the greatest path sum in a triangle using exhaustive search, greedy search, recursive search,
#  and dynamic programming

#  Student's Name: Andrew Dinh

#  Student's UT EID: ad42344

#  Partner's Name: Samuel McKean

#  Partner's UT EID: slm4699

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 12/8/2019

#  Date Last Modified: 12/9/2019

import time
# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):
    sumList = []
    exhaustive_search_helper(grid,sumList,0,0,0)
    return max(sumList)

def exhaustive_search_helper(grid,sumList,row,col,currentSum):
    if row >= len(grid):
        sumList.append(currentSum)
        return
    else:
        exhaustive_search_helper(grid,sumList,row+1,col,currentSum+grid[row][col])
        exhaustive_search_helper(grid,sumList,row+1,col+1,currentSum+grid[row][col])


# returns the greatest path sum using greedy approach
def greedy (grid):
    row = 0
    col = 0
    sum = grid[row][col]
    # selects the greater of the two children to add to the sum
    while row <= len(grid)-2:
        if grid[row+1][col] > grid[row+1][col+1]:
            sum += grid[row+1][col]
        else:
            sum += grid[row+1][col+1]
            col += 1
        row += 1
    return sum

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid):
    return rec_search_helper(grid, 0)

def rec_search_helper (grid, sum):
    if len(grid) == 1:
        return sum + grid[0][0]
    else:
        leftTriangle = []
        rightTriangle = []
        for row in grid[1:]:
            leftTriangle.append(row[1:])
            rightTriangle.append(row[:-1])
        return max(rec_search_helper(leftTriangle, sum+grid[0][0]), rec_search_helper(rightTriangle, sum+grid[0][0]))

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    # creates a triangle to store the maximum sums at each level
    triangle = []
    for i in range(len(grid)-1):
        row = []
        for j in range(i+1):
            row.append(0)
        triangle.append(row)
    triangle.append(grid[-1])
    for i in range(len(triangle)-2,-1,-1):
        for j in range(i+1):
            triangle[i][j] = grid[i][j] + max(triangle[i+1][j],triangle[i+1][j+1])
    return triangle[0][0]

def read_file ():
    with open('triangle.txt', 'r') as inFile:
        numRows = int(inFile.readline())
        triangle = []
        for i in range(numRows):
            triangle.append(list(map(int,inFile.readline().strip().split())))
    return triangle

def main():
    # read triangular grid from file
    triangle = read_file()

    ti = time.time()
    # output greates path from exhaustive search
    print('The greatest path sum through exhaustive search is:', exhaustive_search(triangle))
    tf = time.time()
    del_t = tf - ti
    # print time taken using exhaustive search
    print('The time taken for exhaustive search is:', del_t, '\n')

    ti = time.time()
    # output greates path from greedy approach
    for i in range(1000):
        greedy(triangle)
    print('The greatest path sum through greedy search is:', greedy(triangle))
    tf = time.time()
    del_t = tf - ti
    # print time taken using greedy approach
    print('The time taken for greedy search is:', del_t/1000, '\n')

    ti = time.time()
    # output greates path from divide-and-conquer approach
    print('The greatest path sum through recursive search is:', rec_search(triangle))
    tf = time.time()
    del_t = tf - ti
    # print time taken using divide-and-conquer approach
    print('The time taken for recursive search is:', del_t, '\n')

    ti = time.time()
    # output greates path from dynamic programming
    for i in range(1000):
        dynamic_prog(triangle)
    print('The greatest path sum through dynamic programming is:', dynamic_prog(triangle))
    tf = time.time()
    del_t = tf - ti
    # print time taken using dynamic programming
    print('The time taken for dynamic programming is:', del_t/1000)


if __name__ == "__main__":
    main()
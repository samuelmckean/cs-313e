#  File: Grid.py

#  Description: Given a grid of integers, finds the total number of possible paths from the top left to bottom right.
#               Also finds the greatest path sum and the actual path of with the greatest sum.

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10/10/19

#  Date Last Modified: 10/10/19

# counts all the possible paths in a grid recursively
def count_paths (n, row, col):
    if n == row + 1 or n == col + 1:
        # only one path possible at lower and rightmost edges
        return 1
    else:
        return count_paths(n, row + 1, col) + count_paths(n, row, col + 1)

# recursively gets the greatest sum of all the paths in the grid
def path_sum (grid, n, row, col):
    if n == row + 1 and n == col + 1:
        return grid[row][col]
    elif n == row + 1:
        # path can only come from the right
        return grid[row][col] + path_sum(grid, n, row, col + 1)
    elif n == col + 1:
        # path can only come from the bottom
        return grid[row][col] + path_sum(grid, n, row + 1, col)
    else:
        # choose the greater of the two paths that come from the bottom and right
        return grid[row][col] + max(path_sum(grid, n, row + 1, col), path_sum(grid, n, row, col + 1))

def path_list (grid, n):
    pathSum = [[0 for i in range(n)] for j in range(n)]
    # creates grid of zeros to populate with the greatestPathSum values starting from the bottom right
    for i in range(n - 1, -1, -1):
        for j in range( n - 1, -1 , -1):
            if i == n - 1 and j == n - 1:
                pathSum[i][j] = grid[i][j]
            elif i == n - 1:
                pathSum[i][j] = pathSum[i][j+1] + grid[i][j]
            elif j == n - 1:
                pathSum[i][j] = pathSum[i+1][j] + grid[i][j]
            else:
                pathSum[i][j] = max(pathSum[i+1][j], pathSum[i][j+1]) + grid[i][j]
    greatestSumPath = []
    i = 0
    j = 0
    greatestSumPath.append(grid[i][j])
    # construct actual path starting from the top left and choosing the greater sum values
    while i < n - 1 and j < n - 1:
        if pathSum[i+1][j] > pathSum[i][j+1]:
            greatestSumPath.append(grid[i+1][j])
            i += 1
        else:
            greatestSumPath.append(grid[i][j+1])
            j += 1
    while i < n - 1 or j < n - 1:
        greatestSumPath.append(grid[i][j+1])
        j += 1
    while j < n - 1 or i < n - 1:
        greatestSumPath.append(grid[i+1][j])
        i += 1
    return greatestSumPath

def main():
  # open file for reading
  in_file = open ("./grid.txt", "r")

  # read the dimension of the grid
  dim = in_file.readline()
  dim = dim.strip()
  dim = int(dim)

  # create an empty grid
  grid = []

  # populate the grid
  for i in range (dim):
    line = in_file.readline()
    line = line.strip()
    row = line.split()
    for j in range (dim):
      row[j] = int (row[j])
    grid.append (row)

  # close the file
  in_file.close()

  # get the number of paths in the grid and print
  num_paths = count_paths (dim, 0, 0)
  print ('Number of paths in a grid of dimension', dim, 'is', num_paths)
  print ()

  # get the maximum path sum and print
  max_path_sum = path_sum (grid, dim, 0, 0)
  print ('Greatest path sum is', max_path_sum)
  print ()

  greatestSumPath = path_list(grid, dim)
  print('Actual path is', greatestSumPath)


main()

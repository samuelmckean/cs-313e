#  File: Queens.py

#  Description: Solves all possible solutions for the 8 Queens problem of any
#               size board from 1-8.

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10/20/19

#  Date Last Modified: 10/20/19

class Queens (object):
  # initialize the board
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)
    self.solutions = []

  # appends the board to a list of all board solutions
  def append_board (self):
    current_board = []
    for i in range(self.n):
      row = []
      for j in range(self.n):
        row.append(self.board[i][j])
      current_board.append(row)
    self.solutions.append(current_board)

  # prints the board solutions and number of total solutions
  def print_board (self):
    for i in range(len(self.solutions)):
      for j in range (self.n):
        for k in range (self.n):
          print (self.solutions[i][j][k], end = ' ')
        print ()
      print()

    if len(self.solutions) == 0:
      print("There are no solutions for a {} x {} board.".format(self.n, self.n))
    elif len(self.solutions) == 1:
      print("There is one solution for a {} x {} board.".format(self.n, self.n))
    else:
      print("There are {} solutions for a {} x {} board.".format(len(self.solutions), self.n, self.n))

  # check if no queen captures another
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  # do a recursive backtracking solution
  def recursive_solve (self, col):
    if (col == self.n):
      self.append_board()
    else:
      for i in range (self.n):
        if (self.is_valid(i, col)):
          self.board[i][col] = 'Q'
          self.recursive_solve (col + 1)
          self.board[i][col] = '*'
      return False

  # if the problem has a solution print the board
  def solve (self):
    while self.recursive_solve(0):
        continue
    self.print_board()

def main():
  # prompt and verify user input
  while True:
      try:
        n = int(input("Enter the size of board: "))
        print()
        if n >= 1 and n <= 8:
          break
        else:
          print("Not within range 1-8.")
      except ValueError:
        print("Enter an integer between 1 and 8.")
  
  game = Queens(n)

  # place the queens on the board
  game.solve()

main()

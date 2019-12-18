#  File: MagicSquare.py

#  Description: Creates odd-numbered size magic square from user input. Prints the
#  				square and verifies that all rows, columns, and diagonals match the
# 				canonical sum.

#  Student's Name: Samuel McKean

#  Student's UT EID: slm4699
 
 #  Partner's Name: None

 #  Partner's UT EID: None

 #  Course Name: CS 313E 

 #  Unique Number: 50205

 #  Date Created: 08/30/19

 #  Date Last Modified: 09/03/19

import math

def main():
  # Prompt the user to enter an odd number 1 or greater
	n = eval(input("Please enter an odd number: "))

  # Check the user input
	while not ((n >= 1) and (n % 2 == 1) and (n // 1 == n)):
  		n = eval(input("Invalid number! Enter an odd number 1 or greater: "))

  # Create the magic square
	square = make_square(n)

  # Print the magic square
	print_square(square, n)

  # Verify that it is a magic square
	if check_square(square, n):
		print("\nThis is a magic square and the canonical sum is", n * (n * n + 1) // 2)
	else:
		print("\nThis is not a magic square")


def make_square(n):
  # initialize square with zeros
	square = []
	for i in range(n):
		single_row = []
		for j in range(n):
			single_row.append(0)
		square.append(single_row)

	col = n // 2			# determine middle row of square to start
	row = n - 1				# start on last row
	square[row][col] = 1	# place first number

	for i in range(2, n * n + 1):
	  # save row and col from last number
		prev_row = row
		prev_col = col
	  # find next space to fill
		row += 1
		col += 1
	  # check if row or col off-grid
		if row == n:
			row = 0
		if col == n:
			col = 0
	  # if empty
		if square[row][col] == 0:
	  		square[row][col] = i
	  # if filled
		else:
		  # if space above previous is off grid
			if prev_row == 0:
				square[n-1][prev_col] = i
				row = n - 1		# update row
				col = prev_col	# update col
			else:
				square[prev_row-1][prev_col] = i
				row = prev_row - 1	# update row
				col = prev_col		# update col

	return square
						

def print_square(square, n):
	print("\nhere is a", n, 'x', n, "magic square:\n") 
  # formula to calculate number of digits required for spacing
	largest_num_digits = math.ceil(math.log10(n * n))
  # nested for loop to print magic square
	for i in range(n):
		for j in range(n):
			print(str(square[i][j]).rjust(largest_num_digits), end='  ')
		print('', end='\n')


def check_square(square, n):
	canonical_sum = n * (n * n + 1) // 2
	# check rows and columns
	for i in range(n):
		if sum(square[i]) != canonical_sum:
			return False
		col_sum = 0
		for j in range(n):
			col_sum += square[i][j]
		if col_sum != canonical_sum:
			return False
	# check diagonals
	diagonal1_sum = 0
	diagonal2_sum = 0
	for i in range(n):
		diagonal1_sum += square[i][i]
		diagonal2_sum += square[i][n-1-i]
	if diagonal1_sum != canonical_sum or diagonal2_sum != canonical_sum:
		return False

	return True


	# This line above main is fo
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()

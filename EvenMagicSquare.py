#  File: EvenMagicSquare.py

#  Description: Permutes a 1-D list of consecutive integers recursively to find 
#               the first 10 possible permutations of a 4x4 magic square

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10/13/19

#  Date Last Modified: 10/14/19

# create a global variable to count number of square printed
num_of_squares_printed = 0

# recursively permutes the 1-D list and checks if it is a magic square
# optimized by checking rows to increase efficiency
def permute(square, lo, hi):         
    global num_of_squares_printed

    # base case
    if lo % 4 == 0 and lo != 0:
        # calculate canonical sum
        row_sum = 0
        for i in range(lo - 4, lo):
            row_sum += square[i]
        if row_sum != 34:
            return  # if not equal to canonical sum, break branch
    if lo >= 12:
        # check column for canonical sum
        col_number = lo % 4
        col_sum = 0
        for row in range(4):
            index = row * 4 + col_number
            col_sum += square[index]
        if col_sum != 34:
            return # if not equal to canonical sum, break branch
    if lo == hi:
        magic_square = []
        for i in range(4):
            row = []
            for j in range(4):
                row.append(square[4*i+j])
            magic_square.append(row)
            
        # use check square to verify that the square is a magic square
        if check_square(magic_square, 4):
            num_of_squares_printed += 1
            print(square)
            # if already printed 10 squares, quit
            if num_of_squares_printed == 10:
                quit()
    
    # recursive case
    else:
        for i in range(lo, hi):
            square[i], square[lo] = square[lo], square[i]
            permute(square, lo + 1, hi)
            square[i], square[lo] = square[lo], square[i]

# checks a 2-D list of size n to see if it is a magic square
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

def main():
    magic_square = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    permute(magic_square, 0, len(magic_square))

if __name__ == "__main__":
    main()
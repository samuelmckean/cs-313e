# File: Intervals.py

# Description: Collapses number line intervals and sorts by interval size and lower 				bound using bubble sort algorithm.

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205 

#  Date Created: 09/03/19

#  Date Last Modified: 09/05/19

def main():
	
	# Open file to be read
	inFile = open("intervals.txt", 'r')
	
	# Create empty list for storing tuples
	interval_list = []

	# Read file line by line
	for line in inFile:
		interval_list.append(parseInput(line))
	
	# Sort intervals by lower bound
	interval_list.sort()

	# Initialize counter
	counter = 0

	while counter < len(interval_list) - 1:
		if interval_list[counter][1] >= interval_list[counter+1][0]:
			temp_pair = interval_list.pop(counter+1)
			if interval_list[counter][1] < temp_pair[1]:
				interval_list[counter] = (interval_list[counter][0], temp_pair[1])
		else:
			counter += 1


	# Bubble sort by interval size and lower bound
	interval_list_sorted = bubble_sort(interval_list)

	# Print original sorted list
	print("Non-intersecting Intervals:")
	for i in range(len(interval_list)):
		print(interval_list[i])
	# Print results
	print("\nNon-intersecting Intervals in order of size:")
	for i in range(len(interval_list)):
		print(interval_list_sorted[i])

	inFile.close()



# Takes single line of string values and returns tuple of int
def parseInput(in_value):
	split_list = in_value.split()	# Splits line
	int_list = list(map(int, split_list))	# Converts str to int
	out_value = tuple(int_list)	# Creates tuple from list
	return out_value


# Sorts list of pair by size and lower bound using bubble sort algorithm
def bubble_sort(interval_list):
	pair_list = interval_list[:]	# assign list by value
	change_made = True
	while change_made:
		change_made = False
		for i in range(len(pair_list) - 1):
			if (pair_list[i][1] - pair_list[i][0] > 
			pair_list[i+1][1] - pair_list[i+1][0]):
				pair_list[i], pair_list[i+1] = pair_list[i+1], \
														pair_list[i]
				change_made = True
		print(interval_list)
	
	return pair_list

if __name__ == "__main__":
	main()

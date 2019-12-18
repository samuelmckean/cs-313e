# File: BabyNames.py

#  Description:  

#  Student Name: Samuel McKean 

#  Student UT EID: slm4699

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 09/04/19

#  Date Last Modified: 09/07/19

def main():
	
	# Create empty dict to store names
	baby_names = {}

	# Tuple of decades for data
	decades = (1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970,
				1980, 1990, 2000)

	# Open file and read each line to dict
	inFile = open("names.txt", 'r')
	for line in inFile:
		name_entry = line.split()
		name_entry = ['1001' if x == '0' else x for x in name_entry]
		name = name_entry[0]
		popularity = list(map(int, name_entry[1:]))
		baby_names[name] = popularity

	# User menu
	while True:
		user_choice = menu()

		if user_choice == 1:
			name = input("Enter a name: ")
			print()
			if name_search(name, baby_names):
				print("The matches with their highest ranking decade are:")
				rankings = get_rankings(name, baby_names)
				most_popular_decade = decades[rankings.index(min(rankings))]
				print(name, most_popular_decade, '\n')
			else:
				print("{} does not appear in any decade.".format(name))

		elif user_choice == 2:
			name = input("Enter a name: ")
			rankings = get_rankings(name, baby_names)
			print('\n', name, ': ', sep='', end='')
			print(*rankings, sep=' ')
			for i in range(len(rankings)):
				print(decades[i], rankings[i], sep=": ")
		
		elif user_choice == 3:
			decade_rank(baby_names)	
		
		elif user_choice == 4:
			names_in_all_decades = appear_all_decades(baby_names)
			print(len(names_in_all_decades), 
					"names appear in every decade. The names are:")
			for name in names_in_all_decades:
				print(name)
		
		elif user_choice == 5:
			more_popular(baby_names)
		
		elif user_choice == 6:
			less_popular(baby_names)
		
		elif user_choice == 7:
			break

	print("\nGoodbye.")
	
def menu():

	# Set of valid choices
	valid_choices = {1, 2, 3, 4, 5, 6, 7}

	while True:
	
		# Print out user options
		print("\nOptions:")
		print("1. to search for names.")
		print("2. to display data for one name.")
		print("3. to display all names that appear in one decade.")
		print("4. to display all names that appear in all decades.")
		print("5. to display all names that are more popular in every decade.")
		print("6. to display all names that are less popular in every decade.")
		print("7. to quit.\n")

		try:
			# Ask user input
			user_choice = int(input("Enter choice: "))
		except ValueError:
			print("Invalid input! Select a choice from the menu.\n")
			continue

		if user_choice not in valid_choices:
			print("Invalid input! Select a choice from the menu.\n")
			continue
		
		return user_choice


# Searches database to see if a name exists, returns bool
def name_search(name, data):
	if name in data:
		return True
	return False


# Returns all rankings for a given name
def get_rankings(name, data):
	return data[name]


# Returns list of names that rank in all decades
def appear_all_decades(data):
	names = []
	for name in data:
		if 1001 in data[name]:
			continue
		else:
			names.append(name)
	names.sort()
	return names


# Displays all names with ranking in given decade in order of rank
def decade_rank(data):
	# Tuple of valid decades to verify user input and index dictionary
	valid_decades = (1900, 1910, 1920, 1930, 1940, 1950, 
					1960, 1970, 1980, 1990, 2000)
	while True:
		try:
			decade = int(input("Enter decade: "))
			if decade not in valid_decades:
				print("Please enter a valid decade.")
				continue
		except ValueError:
			print("Please enter an integer.")
			continue
		finally:
			break
	# Find index for specific decade
	decade_index = valid_decades.index(decade)
	# Loop over dictionary to find ranked names
	ranked_names = []	# empty list to append names and values
	for name in data:
		if data[name][decade_index] < 1001:
			ranked_names.append([data[name][decade_index], name])
	# Sort names and print list
	print("The names are in order of rank: ") 
	ranked_names.sort()
	for name in ranked_names:
		print("{}: {}".format(name[1], name[0]))

# Displays all names that are getting more popular every decade
def more_popular(data):
	more_popular_names = []	# initialize empty list
	# Loop over dictionary and add to list if valid
	for name in data:
		# Use to check if more popular
		check = data[name][:]
		check.sort(reverse=True)
		if 1001 not in data[name] and data[name] == check:
			more_popular_names.append(name)
	print(len(more_popular_names), "names are more popular in every decade.")
	for name in more_popular_names:
		print(name)

# Displays all names that are getting less popular every decade
def less_popular(data):
	less_popular_names = []	# initialize empty list
	# Loop over dictionary and add to list if valid
	for name in data:
		# Use to check if more popular
		check = data[name][:]
		check.sort()
		if 1001 not in data[name] and data[name] == check:
			less_popular_names.append(name)
	print(len(less_popular_names), "names are less popular in every decade.")
	less_popular_names.sort()
	for name in less_popular_names:
		print(name)


if __name__ == "__main__":
	main()

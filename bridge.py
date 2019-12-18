#  File: Bridge.py 

#  Description: Determines the fastest crossing time for a group of people who
#               can only cross in pairs and must have the flashlight to cross

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10/3/19

#  Date Last Modified: 10/3/19

def main():
    # read input file
    with open("bridge.txt", 'r') as inFile:
        num_of_cases = int(inFile.readline())
        for i in range(num_of_cases):
            inFile.readline()   # skips line
            num_of_people = int(inFile.readline())
            start = []
            for j in range(num_of_people):
                start.append(int(inFile.readline()))
            start.sort()
            print(min([fastest_carry(start), alternate_method(start)]), '\n')
           
def fastest_carry(start):
    '''
    Solves for the bridge crossing time using the algorithm where the fastest persons carries each other 
    person across every time.
    '''
    if len(start) <= 2:
        return start[-1]
    return start[0] * (len(start) - 2) + sum(start[1:])

def alternate_method(start):
    '''
    Solves for the bridge crossing time using the algorithm where the fastest pair goes first, 
    the fastest brings the flashlight back, then the slowest two cross, and the second fastest brings the
    flashlight back. Repeat until all persons have crossed.
    '''
    time_taken = 0
    end = []
    # loop until only 2 left at start with flashlight
    while len(start) > 2:
        # send fastest 2
        first_over = start.pop(0)
        second_over = start.pop(0)
        time_taken += second_over
        end.insert(0, second_over)
        end.insert(0, first_over)
        # send fastest back
        fastest_back = end.pop(0)
        time_taken += fastest_back
        start.insert(0, fastest_back)

        # check if only 2 and flashlight
        if len(start) <= 2:
            break
        # send slowest two
        slowest_over = start.pop()
        second_slowest_over = start.pop()
        time_taken += slowest_over
        end.append(second_slowest_over)
        end.append(slowest_over)
        # send fastest (second fastest overall) back
        fastest_back = end.pop(0)
        time_taken += fastest_back
        start.insert(1, fastest_back)

    # add time for last remaining 2
    time_taken += start[-1]
    return time_taken



if __name__ == "__main__":
    main()

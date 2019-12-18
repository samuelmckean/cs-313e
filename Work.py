# File: Work.py

# Description: Calculates the minimum lines of codes needing to be written by a procrastinating student before
#              taking his first cup of coffee to be able to finish his assignment of n lines.

# Student Name: Samuel McKean

# Student UT EID: slm4699

# Course Name: CS 313E

# Unique Number: 50205

# Date Created: 9/26/19

# Date Last Modified: 9/26/19

def main():
    # read the file
    with open("work.txt", 'r') as inFile:
        T = int(inFile.readline())
        test_cases = []
        for i in range(T):
            test_cases.append(tuple(map(int, inFile.readline().strip().split())))
            print(binary_search(test_cases[i][0], test_cases[i][1]))


def binary_search(n, k):
    v_list = range(n+1)
    low = 0
    high = len(v_list)
    mid = (low + high) // 2
    while low < high:
        # check if higher or lower than current mid
        if total_lines(v_list[mid], k) < n:
            low = mid + 1
        elif total_lines(v_list[mid], k) > n:
            high = mid
        else:
            return v_list[mid]
        mid = (low + high) // 2
    return mid


def total_lines(v, k):
    '''
    Returns the total number of lines the student will write if he/she writes v lines on the first attempt and has
    productivity factor of k.
    '''
    total_lines = 0
    i = 0
    while True:
        total_lines += v // k**i
        i += 1
        if v // k**i <= 0:
            break
    return total_lines


if __name__ == "__main__":
    main()

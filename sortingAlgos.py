'''
Has functions for selection, bubble, insertion, merge, and quick sort algorithms.
Main tests and times these for random lists of different lengths.
'''
from random import randint
import time

def selection_sort(a):
    '''
    Iterates through the list to find the next lowest value and places the value in its proper spot.
    '''
    for i in range(len(a)):
        min_value = a[i]
        min_value_index = i
        for j in range(i + 1, len(a)):
            if a[j] < min_value:
                min_value = a[j]
                min_value_index = j
        a[i], a[min_value_index] = a[min_value_index], a[i]
    return a

def bubble_sort(a): 
    ''' 
    Bubbles the smallest value to the front by swapping adjacent elements.  
    ''' 
    for i in range(len(a) - 1): 
        swapped = False 
        for j in range(len(a) - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def insertion_sort(a):
    '''
    Partitions the list into a sorted and an unsorted part. Takes the next value of the unsorted part
    and inserts it into its proper spot in the sorted part.
    '''
    for i in range(1, len(a)):
        for j in range(i):
            if a[i] < a[j]:
                a.insert(i, a.pop(j))
    return a

def merge_sort(a):
    '''
    Sorts a list using recursion to sort each half of the list and then merging the two halves in the proper order.
    '''
    # split the list in half and then merge both halves
    middle = len(a) // 2
    if len(a) <= 1:
        return a
    else:
        return merge(merge_sort(a[:middle]), merge_sort(a[middle:]))

def merge(a, b):
    '''
    Merges two sorted lists and returns the merged list.
    '''
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    # if b is empty but a is still full
    if i < len(a):
        for idx in range(i, len(a)):
            c.append(a[idx])
    # if a is empty but b is still full
    else:
        for idx in range(j, len(b)):
            c.append(b[idx])
    return c

def quick_sort(a):
    '''
    Uses the first value as the pivot point, moving all values lower than pivot to the left and moving all values
    greater than the pivot to the right. Uses recursion to sort the two halves.
    '''
    quick_sort_helper(a, 0, len(a) - 1)
    return a

def quick_sort_helper(a, lo, hi):
    if lo >= hi:
        return
    else:
        p = a[lo]
        p_idx = lo
        for i in range(lo + 1, hi + 1):
            if a[i] < p:
                # if less than pivot, move the value to the left part of the list, and increment pivot index
                p_idx += 1
                a[i], a[p_idx] = a[p_idx], a[i]
        # swap pivot (first element) with the last element of left half of list to put pivot in its proper spot
        a[lo], a[p_idx] = a[p_idx], a[lo]
        # recursively sort both halves
        quick_sort_helper(a, lo, p_idx)
        quick_sort_helper(a, p_idx+1, hi)
    
def main():
    # initialize variables for sorting execution times
    selection_sort_time = 0
    bubble_sort_time = 0
    insertion_sort_time = 0
    merge_sort_time = 0
    quick_sort_time = 0

    # do 100 trials
    for i in range(100):
        # Generate lists of random integers of lengths 10, 100, and 1000
        a = [randint(0, 100) for i in range(10)]
        b = [randint(0, 1000) for i in range(100)]
        c = [randint(0, 10000) for i in range(1000)]

        # Selection sort
        selection_start_time = time.process_time()
        selection_sort(a[:])
        selection_sort(b[:])
        selection_sort(c[:])
        selection_sort_time += time.process_time() - selection_start_time
        
        # Bubble sort
        bubble_start_time = time.process_time()
        bubble_sort(a[:])
        bubble_sort(b[:])
        bubble_sort(c[:])
        bubble_sort_time += time.process_time() - bubble_start_time
        
        # Insertion sort
        insertion_start_time = time.process_time()
        insertion_sort(a[:])
        insertion_sort(b[:])
        insertion_sort(c[:])
        insertion_sort_time += time.process_time() - insertion_start_time

        # Merge sort
        merge_start_time = time.process_time()
        merge_sort(a[:])
        merge_sort(b[:])
        merge_sort(c[:])
        merge_sort_time += time.process_time() - merge_start_time

        # Quick sort
        quick_start_time = time.process_time()
        quick_sort(a[:])
        quick_sort(b[:])
        quick_sort(c[:])
        quick_sort_time += time.process_time() - quick_start_time

    # print execution times
    print("Selection:", selection_sort_time)
    print("Bubble:", bubble_sort_time)
    print("Insertion:", insertion_sort_time)
    print("Merge:", merge_sort_time)
    print("Quick:", quick_sort_time)

if __name__ == "__main__":
    main()

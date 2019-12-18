#  File: TestLinkedList.py

#  Description: Creates and tests LinkedList and Link classes.

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10/31/19

#  Date Last Modified: 10/31/19

class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__ (self):
        self.first = None

    def get_num_links(self):
        counter = 0
        current = self.first
        while current != None:
            counter += 1
            current = current.next
        return counter

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)
        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)
        current = self.first
        if current == None:
            self.first = new_link
            return
        while current.next != None:
            current = current.next
        current.next = new_link

    # add an item in an ordered list in ascending order
    def insert_in_order(self, data):
        current = self.first
        if current == None or current.data >= data:
            self.insert_first(data)
            return
        while current.next != None and current.next.data <= data:
            current = current.next
        link = Link(data,current.next)
        current.next = link
        return

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        current = self.first
        if current == None:
            return None
        while current.data != data:
            if current.next == None:
                return None
            else:
                current = current.next
        return True

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        current = self.first
        while current != None and current.data <= data:
            if current.data == data:
                return True
            current = current.next
        return None

    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, data):
        previous = self.first
        current = self.first
        if current == None:
            return None
        while current.data != data:
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next
        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next
        return current

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        string = ''
        current = self.first
        while current != None:
            string += str(current.data) + '  '
            current = current.next
        return string

    # Copy the contents of a list and return new list
    def copy_list(self):
        current = self.first
        copyList = LinkedList()
        while current != None:
            copyList.insert_last(current.data)
            current = current.next
        return copyList

    # Reverse the contents of a list and return new list
    def reverse_list(self):
        current = self.first
        reverseList = LinkedList()
        while current != None:
            reverseList.insert_first(current.data)
            current = current.next
        return reverseList

    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        sortedList = LinkedList()
        current = self.first
        while current != None:
            sortedList.insert_in_order(current.data)
            current = current.next
        return sortedList

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        current = self.first
        while current.next != None:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        if self.first == None:
            return True
        return False

    # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):
        mergedList = LinkedList()
        #creates pointers for each linked list
        currentA = self.first
        currentB = other.first
        while currentA != None and currentB != None:
            #inserts lower of two pointers into new list
            if currentA.data >= currentB.data:
                mergedList.insert_last(currentB.data)
                currentB = currentB.next
            else:
                mergedList.insert_last(currentA.data)
                currentA = currentA.next
        #inserts the remaining elements after one list is depleted
        if currentA == None:
            while currentB != None:
                mergedList.insert_last(currentB.data)
                currentB = currentB.next
        if currentB == None:
            while currentA != None:
                mergedList.insert_last(currentA.data)
                currentA = currentA.next
        return mergedList

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        currentA = self.first
        currentB = other.first
        if self.get_num_links() != other.get_num_links():
            return False
        while currentA != None:
            if currentA.data != currentB.data:
                return False
            currentA = currentA.next
            currentB = currentB.next
        return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):
        newList = LinkedList()
        current = self.first
        while current != None:
            if newList.find_unordered(current.data):
                current = current.next
                continue
            newList.insert_last(current.data)
            current = current.next
        return newList


def main():
    testList = LinkedList()
    for num in range(9,-1,-1):
        testList.insert_first(num)
    print(testList)
# Test methods insert_first() and __str__() by adding more than
# 10 items to a list and printing it.
    testList.insert_last(10)
    print(testList)
# Test method insert_last()
    testList.insert_in_order(7)
    print(testList)
# Test method insert_in_order()
    print(testList.get_num_links())
# Test method get_num_links()
    print(testList.find_unordered(100))
    print(testList.find_unordered(7))
# Test method find_unordered()
# Consider two cases - data is there, data is not there
    print(testList.find_unordered(100))
    print(testList.find_ordered(7))
# Test method find_ordered()
# Consider two cases - data is there, data is not there
    print(testList.delete_link(100))
    print(testList.delete_link(7).data)
# Test method delete_link()
# Consider two cases - data is there, data is not there
    print(testList.copy_list())
# Test method copy_list()
    print(testList.reverse_list())
# Test method reverse_list()
    unsortedList = LinkedList()
    for i in [5,2,7,4,3,6,8,2,5]:
        unsortedList.insert_first(i)
    print(unsortedList.sort_list())
# Test method sort_list()
    print(unsortedList.is_sorted())
    print(testList.is_sorted())
# Test method is_sorted()
# Consider two cases - list is sorted, list is not sorted
    emptyList = LinkedList()
    print(emptyList.is_empty())
    print(testList.is_empty())
# Test method is_empty()
    listA = LinkedList()
    listB = LinkedList()
    for i in [1,3,6,7,7,9]:
        listA.insert_last(i)
    for i in [1,4,4,5,6,8]:
        listB.insert_last(i)
    print(listA.merge_list(listB))
# Test method merge_list()
    print(testList.is_equal(listA))
    print(testList.is_equal(testList.copy_list()))
# Test method is_equal()
# Consider two cases - lists are equal, lists are not equal
    print(listA.merge_list(listB).remove_duplicates())
# Test remove_duplicates()

if __name__ == "__main__":
    main()

#  File: Josephus.py

#  Description: Solves the Josephus' problem given an input file with the 
#               number of soldiers, starting number, and elimination number.

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11/2/19

#  Date Last Modified: 11/2/19

class Link(object):
  def __init__(self, data, next=None):
    self.data = data
    self.next = next


class CircularList(object):
  # Constructor
  def __init__ (self): 
    self.start = None
    self.size = 0

  # Insert an element (value) in the list
  def insert(self, data):
    link = Link(data)
    if self.size == 0:
      self.first = link
      link.next = link
    else:
      current = self.first
      while current.next != self.first:
        current = current.next
      current.next = link
      link.next = self.first
    self.size += 1

  # Find the link with the given data (value)
  def find(self, data):
    current = self.first
    if current.data == data:
      return current
    current = current.next
    while current.data <= data and current != self.first:
      if current.data == data:
        return current
      current = current.next
    return None

  # Delete a link with a given data (value)
  def delete(self, data):
    link = self.find(data)
    if link != None:
      previous = link
      previous = previous.next
      while previous.next != link:
        previous = previous.next
      previous.next = link.next
      print(link.data)
      if link == self.first:
        self.first = link.next
      self.size -= 1

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def delete_after(self, start, n):
    current = self.find(start)
    for i in range(n-1):
      current = current.next
    next_link = current.next
    self.delete(current.data)
    return next_link.data

  # Return a string representation of a Circular List
  def __str__ (self):
    current = self.first.next
    circle_list = str(self.first.data) + "  "
    while current != self.first:
      circle_list += str(current.data) + "  "
      current = current.next
    return circle_list

def main():
  # read data from file
  with open("josephus.txt", 'r') as in_file:
    num_soldiers = int(in_file.readline())
    start_position = int(in_file.readline())
    increment = int(in_file.readline())
    
  # create circle of soldiers
  circle = CircularList()
  for i in range(num_soldiers):
    circle.insert(i+1)

  # starting at start_position, eliminate every increment soldier
  while circle.size > 0:
    start_position = circle.delete_after(start_position, increment)

main()
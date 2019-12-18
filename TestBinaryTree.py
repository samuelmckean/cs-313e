#  File: TestBinaryTree.py

#  Description: Defines and tests a BST class with methods is_similar,
#               print_level, get_height, and num_nodes.

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11/20/19

#  Date Last Modified: 11/20/19

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def is_empty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Node (object):
  def __init__(self, data):
    self.data = data
    self.left_child = None
    self.right_child = None

class Tree (object):
  def __init__(self):
    self.root = None

  # the insert() function adds a node containing data in
  # the binary search tree.
  def insert (self, data):
    if self.root == None:
      self.root = Node(data)
      return
    previous = self.root
    current = self.root
    while current != None:
      previous = current
      if data == current.data:
        return
      elif data > current.data:
        current = current.right_child
      else:
        current = current.left_child     
    if data > previous.data:
      previous.right_child = Node(data)
    else:
      previous.left_child = Node(data)

  # Returns true if two binary trees are similar
  def is_similar (self, pNode):
    self_stack = Stack()
    p_stack = Stack()
    self_stack.push(self.root)
    p_stack.push(pNode)
    while not self_stack.is_empty() and not p_stack.is_empty():
      cur_self = self_stack.pop()
      cur_p = p_stack.pop()
      if (cur_self == None and cur_p != None) or (cur_self != None and cur_p == None):
        return False
      elif cur_self == None and cur_p == None:
        continue
      if cur_self.data != cur_p.data:
        return False
      self_stack.push(cur_self.left_child)
      self_stack.push(cur_self.right_child)
      p_stack.push(cur_p.left_child)
      p_stack.push(cur_p.right_child)
    if self_stack.is_empty() and p_stack.is_empty():
      return True
    return False

  # Prints out all nodes at the given level
  def print_level (self, level):
    stack = Stack()
    stack.push(self.root)
    for i in range(level - 1):
      items = []
      while not stack.is_empty():
        items.insert(0, stack.pop())
      for item in items:
        if item != None:
          stack.push(item.right_child)
          stack.push(item.left_child)
    s = ''
    while not stack.is_empty():
      if stack.peek() == None:
        stack.pop()
      else:
        s += str(stack.pop().data) + ' '
    return s

  # Returns the height of the tree
  def get_height (self):
    return self.get_height_helper(self.root)

  def get_height_helper(self, node):
    #  base case
    if node == None:
      return 0
    else:
      left_height = self.get_height_helper(node.left_child) + 1
      right_height = self.get_height_helper(node.right_child) + 1
      return max([left_height, right_height])

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
    return self.num_nodes_helper(self.root)

  def num_nodes_helper(self, node):
    # base case
    if node == None:
      return 0
    else:
      return self.num_nodes_helper(node.left_child) + self.num_nodes_helper(node.right_child) + 1

def main():
    # Create three trees - two are the same and the third is different
    a = [50, 30, 70, 10, 40, 80, 20]
    b = [50, 30, 70, 10, 40, 80, 20]
    c = [50, 30, 70, 10, 40, 60, 80, 20, 15]
    tree_a = Tree()
    for n in a:
      tree_a.insert(n)
    tree_b = Tree()
    for n in b:
      tree_b.insert(n)
    tree_c = Tree()
    for n in c:
      tree_c.insert(n)

    # Test your method is_similar()
    print(tree_a.is_similar(tree_b.root))

    # Print the various levels of two of the trees that are different
    for i in range(1, 5):
      print("A:", tree_a.print_level(i))
      print("B:", tree_c.print_level(i))

    # Get the height of the two trees that are different
    print(tree_a.get_height())
    print(tree_c.get_height())

    # Get the total number of nodes a binary search tree
    print(tree_a.num_nodes())
    print(tree_c.num_nodes())

main()
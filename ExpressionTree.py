#  File: ExpressionTree.py

#  Description: Creates an expression tree from an infix expression. Evaluates
#               the expression and prints pre-fix and post-fix notations.

#  Student's Name: Samuel McKean

#  Student's UT EID: slm4699

#  Partner's Name: Andrew Dinh

#  Partner's UT EID: ad42344

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 11/14/19

#  Date Last Modified: 11/14/19

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
  def __init__ (self):
    self.root = Node(None)
    self.operators = {'+', '-', '*', '/', '//', '%', '**'}

  def create_tree (self, expr):
    cur = self.root
    stack = Stack()
    for token in expr:
      if token == '(':
        cur.left_child = Node(None)
        stack.push(cur)
        cur = cur.left_child
      elif token in self.operators:
        cur.data = token
        stack.push(cur)
        cur.right_child = Node(None)
        cur = cur.right_child
      elif token == ')':
        if not stack.is_empty():
          cur = stack.pop()
      else:
        if float(token) // 1 == float(token):
          cur.data = int(token)
        else:
          cur.data = float(token)
        cur = stack.pop()

  def evaluate (self, aNode):
    cur = aNode
    if cur.data not in self.operators:
      return cur.data
    a =  self.evaluate(cur.left_child)
    b = self.evaluate(cur.right_child)

    # evaluate a operator b
    if cur.data == '+':
      return a + b
    elif cur.data == '-':
      return a - b
    elif cur.data == '*':
      return a * b
    elif cur.data == '/':
      return a / b
    elif cur.data == '//':
      return a // b
    elif cur.data == '%':
      return a % b
    elif cur.data == '**':
      return a ** b

  def pre_order (self, aNode):
    cur = aNode
    expr = ''
    # cur is operators
    if cur.data in self.operators:
      expr += cur.data + ' '
      expr += self.pre_order(cur.left_child)
      expr += self.pre_order(cur.right_child)
      return expr
    # cur is operand
    expr += str(cur.data) + ' '
    return expr

  def post_order (self, aNode):
    cur = aNode
    expr = ''
    # cur is operators
    if cur.data in self.operators:
      expr += self.post_order(cur.left_child)
      expr += self.post_order(cur.right_child)
      expr += cur.data + ' '
      return expr
    # cur is operand
    expr += str(cur.data) + ' '
    return expr


def main():
  with open('expression.txt', 'r') as in_file:
    expr_str = in_file.readline().strip()
    expr = expr_str.split()
  
  tree = Tree()
  tree.create_tree(expr)

  print(expr_str, '=', tree.evaluate(tree.root))
  print('Prefix Expression:', tree.pre_order(tree.root))
  print('Postfix Expression:', tree.post_order(tree.root))

if __name__ == "__main__":
    main()

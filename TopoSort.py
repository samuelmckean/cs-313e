#  File: TopoSort.py

#  Description: Extends the Graph class to include has_cycle and toposort methods.
#               Main function tests these methods.

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 12/1/19

#  Date Last Modified: 12/1/19


class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check the item on the top of the stack
  def peek (self):
    return self.queue[0]

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))


class Vertex:
  def __init__ (self, label):
    self.label = label
    self.visited = False
    self.visited_this_search = False
    self.added_to_topo_stack = False
    self.level = 100

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)


class Graph:
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (not self.has_vertex (label)):
      self.Vertices.append (Vertex (label))

    # add a new column in the adjacency matrix
    nVert = len (self.Vertices)
    for i in range (nVert - 1):
      (self.adjMat[i]).append (0)

    # add a new row for the new vertex
    new_row = []
    for i in range (nVert):
      new_row.append (0)
    self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    for v in range(len(self.Vertices)):
      if start == self.Vertices[v].label:
        start = v
      if finish == self.Vertices[v].label:
        finish = v
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # return a list of all adjacent vertices to vertex v (index)
  def get_all_adj_vertices(self, v):
    nVert = len(self.Vertices)
    adj_vertices = []
    for i in range(nVert):
      if (self.adjMat[v][i] > 0):
        adj_vertices.append(i)
    return adj_vertices

  # return a list of all the incoming vertices to vertex v (index)
  def get_all_incoming_vertices(self, v):
    nVert = len(self.Vertices)
    adj_vertices = []
    for i in range(nVert):
      if (self.adjMat[i][v] > 0):
        adj_vertices.append(i)
    return adj_vertices

  # do a depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do the breadth first search in a graph
  def bfs (self, v):
    # create the Queue
    theQueue = Queue ()

    # mark the vertex v as visited and enqueue it
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theQueue.enqueue (v)

    # visit all the other vertices according to breadth
    while (not theQueue.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theQueue.peek())
      if (u == -1):
        u = theQueue.dequeue()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theQueue.enqueue (u)

    # the queue is empty, let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # delete an edge from the adjacency matrix
  # delete a single edge if the graph is directed
  # delete two edges if the graph is undirected
  def delete_edge (self, fromVertexLabel, toVertexLabel):
    # determine if graph is directed or undirected
    directed = False
    for i in range(len(self.adjMat)):
      for j in range(len(self.adjMat)):
        if self.adjMat[i][j] != self.adjMat[j][i]:
          directed = True

    # get indices for the two vertices
    from_vertex_index = self.get_index(fromVertexLabel)
    to_vertex_index = self.get_index(toVertexLabel)

    # update the adjacency matrix by changing the one element if directed or
    # two corresponding elements if undirected to zeros
    if directed:
      self.adjMat[from_vertex_index][to_vertex_index] = 0
    else:
      self.adjMat[from_vertex_index][to_vertex_index] = 0
      self.adjMat[to_vertex_index][from_vertex_index] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def delete_vertex (self, vertexLabel):
    # find index of Vertex
    index = self.get_index(vertexLabel)

    # remove row from adjacency matrix
    self.adjMat = self.adjMat[:index] + self.adjMat[index+1:]

    # remove column from adjacency matrix
    for i in range(len(self.adjMat)):
      self.adjMat[i] = self.adjMat[i][:index] + self.adjMat[i][index+1:]

    # remove vertex from self.Vertices
    self.Vertices = self.Vertices[:index] + self.Vertices[index+1:]

  # determine if a directed graph has a cycle
  # this function should return a boolean and not print the result
  def has_cycle (self):
    # do dfs for starting at all vertices
    for v in range(len(self.Vertices)):
      # create the Stack
      theStack = Stack ()

      # mark the vertex v as visited and push it on the Stack
      (self.Vertices[v]).visited = True

      # mark vertex v as visited this search
      self.Vertices[v].visited_this_search = True

      # get all adjacent vertices and check if any are visited
      adj_vertices = self.get_all_adj_vertices(v)
      for vertex in adj_vertices:
        if self.Vertices[vertex].visited_this_search == True:
          return True
      theStack.push (v)

      # visit all the other vertices according to depth
      while (not theStack.is_empty()):
        # get an adjacent unvisited vertex
        u = self.get_adj_unvisited_vertex (theStack.peek())

        if (u == -1):
          u = theStack.pop()
          adj_vertices = self.get_all_adj_vertices(u)
          for y in adj_vertices:
            self.Vertices[y].visited_this_search = False
        else:
          self.Vertices[u].visited_this_search = True
          # get all adjacent vertices and check if any are visited
          if self.Vertices[u].visited == False:
            adj_vertices = self.get_all_adj_vertices(u)
            for vertex in adj_vertices:
              if self.Vertices[vertex].visited_this_search == True:
                # reset all visited this search flags
                for vertex in range(len(self.Vertices)):
                  self.Vertices[vertex].visited_this_search = False
                # reset visited flags
                for i in range (nVert):
                  (self.Vertices[i]).visited = False
                return True
          (self.Vertices[u]).visited = True
          theStack.push (u)
        
      # the stack is empty, let us reset the flags
      nVert = len (self.Vertices)
      for i in range (nVert):
        (self.Vertices[i]).visited = False

      # if no cycles found, return False
      return False

  # return a list of vertices after a topological sort
  # this function should not print the list
  def toposort (self):
    # copy the graph object
    graph_copy = Graph()
    graph_copy.Vertices = self.Vertices[:]
    graph_copy.adjMat = self.adjMat[:][:]

    # topographically sort
    empty_list = []
    while len(graph_copy.Vertices) != 0:
      level_list = []
      # find vertices with in-degree of 0
      for vertex in graph_copy.Vertices:
        index = graph_copy.get_index(vertex.label)
        if len(graph_copy.get_all_incoming_vertices(index)) == 0:
          level_list.append(vertex.label)

      # sort each level alphabetically
      level_list.sort()
      empty_list.extend(level_list)
      for label in level_list:
        graph_copy.delete_vertex(label)
    return empty_list


def main():
  # create the Graph object
  cities = Graph()

  # oepn the file for reading
  in_file = open ("./topo.txt", "r")

  # read the number of vertices
  num_vertices = int ((in_file.readline()).strip())

  # read all the Vertices and add them the Graph
  for i in range (num_vertices):
    city = (in_file.readline()).strip()
    cities.add_vertex (city)

  # read the number of edges
  num_edges = int ((in_file.readline()).strip())

  # read the edges and add them to the adjacency matrix
  for i in range (num_edges):
    edge = (in_file.readline()).strip()
    edge = edge.split()
    start = edge[0]
    finish = edge[1]

    cities.add_directed_edge (start, finish)

  # test if a directed graph has a cycle
  print("The Graph has a cycle.\n" if cities.has_cycle() else "The Graph does not have a cycle.\n")

  # test topological sort
  if not cities.has_cycle():
    print("List of vertices after toposort")
    print(cities.toposort())

main()
from graph import Graph
from util import Stack, Queue

# Step 1: Translate problem into graph terminology
# We have 11 vertices, each vertex can have up to two parents.
# Using the below diagram, we'll start at the bottom of the diagram and create a graph
# using one way edges from the lowest vertex in the tree up to the highest vertex in the tree.

"""
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
"""

# Step 2: Build your graph

graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)
graph.add_vertex(8)
graph.add_vertex(9)
graph.add_vertex(10)
graph.add_vertex(11)
graph.add_edge(6, 3)
graph.add_edge(6, 5)
graph.add_edge(3, 1)
graph.add_edge(3, 2)
graph.add_edge(1, 10)
graph.add_edge(5, 4)
graph.add_edge(7, 5)
graph.add_edge(9, 8)
graph.add_edge(8, 4)
graph.add_edge(8, 11)

# See graph
print(graph.vertices)

# Step 3 traverse your graph.

"""
Write a function that, given the dataset and the ID of an individual in the dataset, 
returns their earliest known ancestor – the one at the farthest distance from the input individual. 
If there is more than one ancestor tied for "earliest", 
return the one with the lowest numeric ID. 
If the input individual has no parents, the function should return -1.
"""






















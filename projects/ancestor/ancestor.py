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

"""
Write a function that, given the dataset and the ID of an individual in the dataset, 
returns their earliest known ancestor – the one at the farthest distance from the input individual. 
If there is more than one ancestor tied for "earliest", 
return the one with the lowest numeric ID. 
If the input individual has no parents, the function should return -1.
"""

def earliest_ancestor(list, starting_vertex):
    # Step 2: Build your graph.
    graph = Graph()
    num_of_vert = 1
    # Creates a vertex for each tuple in the list.
    for atup in list:
        graph.add_vertex(num_of_vert)
        num_of_vert += 1
    # Creates an edge using the connection listed in each tuple.
    for atup in list:
        vert = atup[1]
        # If the number at the zeroeth index of the tuple isn't a vertex, add it as a vertex.
        if atup[0] not in graph.vertices:
            graph.add_vertex(atup[0])
        graph.add_edge(vert, atup[0])
            

    # Step 3: Traverse your graph.
    # Performs a depth first search to find the earliest ancestor
    visited = set()
    stack = Stack()
    stack.push(starting_vertex)
    travelled = False

    while stack.size() > 0:
        # If both parent vertexes don't have any parent vertexes, compare the two parent vertexes and return the parent vertex that is smaller.
        try:
            if len(graph.vertices[stack.stack[0]]) == 0 and len(graph.vertices[stack.stack[1]]) == 0 and stack.stack[0] > stack.stack[1]:
                return stack.stack[1]
            elif len(graph.vertices[stack.stack[0]]) == 0 and len(graph.vertices[stack.stack[1]]) == 0 and stack.stack[0] < stack.stack[1]: 
                return stack.stack[0]
        except IndexError:
            pass
        v = stack.pop()
        size = stack.size() # size of stack
        num_of_parents = len(graph.vertices[v]) # number of parents that current vertex has.
        # If we haven't visited this vertex yet, place this vertex in visited.
        if v not in visited:
            visited.add(v)
            # If the number of parents is zero, and we haven't travelled up the adjacency list, and we don't have any parents left to check
            # Return -1, because this means we didn't travel, but there are also no parents to check.
            if num_of_parents == 0 and not travelled and size == 0:
                return -1
            # If there are no parents to check, and we travelled, and we don't have any other parents to check
            # Return that vertex, because it means it's our earliest ancestor.
            elif num_of_parents == 0 and travelled and size == 0:
                return v
            # If neither of the above are true, it means there are parents to check, so add each parent to our stack and start
            # at the top of the DFS. 
            else:
                for neighbor in graph.vertices[v]:
                    stack.push(neighbor)
                    travelled = True
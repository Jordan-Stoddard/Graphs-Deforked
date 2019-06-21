from graph import Graph
from util import Stack, Queue

def earliest_ancestor(ancestors, starting_index):
    # build the graph
    # build edges in reverse
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])


    # (track the longest paths length and the earliest ancestor node)
    max_path_len = 1
    earliest_ancestor = -1
    # Do a BFS from starting_node to each other node.
    q = Queue()
    q.enqueue([starting_node])
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
    # if path is longer or path is same length and node is smaller
    if (len(path) == max_path_len and v < earliest_ancestor) or (len(path) > max_path_length):
        earliest_ancestor = v
        max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(past)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    # Return the earliest ancestor.
    return earliest_ancestor
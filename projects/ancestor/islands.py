'''
Write a function that takes a 2D binary array and
returns the number of 1 islands. An island consists
of 1s that are connected to the north, south, east
or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4
'''

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

# islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
#            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
#            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
#            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
#            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
#            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
#            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
#            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
#            [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
#            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]



# 1. Translate problem into graph terminology:



# 2. Build your graph

def get_neighbors(v, matrix):
    col = v[0]
    row = v[1]
    neighbors = []
    # Check North
    if row > 0 and matrix[row - 1][col] == 1:
        neighbors.append((col, row-1))
    # Check South
    if row < len(matrix) - 1 and matrix[row + 1][col] == 1:
        neighbors.append((col, row+1))
    # Check East
    if col < len(matrix[0]) - 1 and matrix[row][col + 1]:
        neighbors.append((col + 1, row))
    # Check West
    if col > 0 and matrix[row][col - 1]:
        neighbors.append((col - 1, row))
    return neighbors




# 3. Traverse your graph

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


def island_counter(matrix):
    # Create a visited matrix
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    island_count = 0
    # Walk through each cel in the matrix
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            # If that cel has not been visited
            if not visited[row][col]:
                # When I reach a 1,
                if matrix[row][col] == 1:
                    # Do a DFT and mark each as visited
                    visited = dft(col, row, matrix, visited)
                    # Then increment the counter by 1
                    island_count += 1
    # Return island count
    return island_count



def dft(col, row, matrix, visited):
    s = Stack()
    s.push((col, row))
    while s.size() > 0:
        v = s.pop()
        col = v[0]
        row = v[1]
        if not visited[row][col]:
            visited[row][col] = True
            for neighbor in get_neighbors(v, matrix):  # STUB
                s.push(neighbor)
    return visited



print(island_counter(islands))
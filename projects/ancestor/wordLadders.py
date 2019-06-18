from util import Stack, Queue
#STEPS TO SOLVE (almost) ANY GRAPHS PROBLEM!
#* Translate the problem into graph terminology
#* Build your graph
#* Traverse your graph

WordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
word_set = set(['hot', 'dot', 'dog', 'lot', 'log', 'cog'])
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'x', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_neighbors(word):
    # create an empty neighbors list
    neighbors = []
    # turn our word into an array of characters
    string_word = list(word)
    # For each letter in the word
    for i in range(len(string_word)):
    # for each letter in the alphabet...
        for letter in letters:
        # swap that letter with a letter in the alphabet
            temp_word = list(string_word)
            temp_word[i] = letter
        # Reform it into a word string and check if it's in word_set
        w = "".join(temp_word)
        # if it doesn't equal the original word and it's in the ste, add to neighbors
        if w != word and w in word_set:
            neighbors.append(w)
    return neighbors


# Implement our traversal
def find_ladders(beginWord, endWord):
    visited = set()
    q = Queue()
    q.enqueue([beginWord])
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            if v == endWord:
                return path
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)
# get neighbors function
    return None

print(find_ladders('hit', 'cog'))
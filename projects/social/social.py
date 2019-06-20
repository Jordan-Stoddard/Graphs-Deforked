import random
import math
import time
from util import Stack, Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        if numUsers < avgFriendships:
            return 'Number of users must be greater than avg friendships.'

        # Add users
        # Creates a social graph 
        for i in range(0, numUsers):
            self.addUser(i)

        # Create friendships
        # Total possible friendships will be numUsers * avg friendships (10 * 2) = 20
        # Max number of friends per user to create average will be numUsers / avg friendships (10 / 2) = 5
        # (So with the example of populateGraph(10, 2): 
        # We would need somewhere between 0 and 4 friendships per user, with a max number of friendships across all users being 20)
        max_friendships = numUsers * avgFriendships
        max_friends_per_user = math.floor(numUsers / avgFriendships)
        current_num_friendships = 0
        # Need a way to generate a random set of friends for that user.
        while current_num_friendships < max_friendships:
            for user in self.friendships:
            # generate a random number of friendships up to the max friends per user
                for i in range(0, random.randint(0, max_friends_per_user -1)):
                    randomFriend = random.randint(1, self.lastID)
                    if randomFriend > user and randomFriend not in self.friendships[user] and len(self.friendships[user]) + 1 <= max_friends_per_user - 1:
                        if current_num_friendships == max_friendships:
                            break
                        else:
                            self.addFriendship(user, randomFriend)
                            current_num_friendships += 2
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
    def getAllSocialPaths(self, userID):
        visited = {}  # Note that this is a dictionary, not a set
        q = Queue()
        q.enqueue([userID])

        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                visited.update({v: path})
                for neighbor in self.friendships[v]:
                    # if neighbor not in visited:
                        path_copy = path.copy()
                        path_copy.append(neighbor)
                        q.enqueue(path_copy)
        return visited


        # def populateGraphLinear(self, numUsers, avgFriendships):
        # """
        # Takes a number of users and an average number of friendships
        # as arguments

        # Creates that number of users and a randomly distributed friendships
        # between those users.

        # The number of users must be greater than the average number of friendships.
        # """
        # # Reset graph
        # self.lastID = 0
        # self.users = {}
        # self.friendships = {}
        # # !!!! IMPLEMENT ME
        # if numUsers < avgFriendships:
        #     return 'Number of users must be greater than avg friendships.'

        # # Add users
        # # Creates a social graph 
        # for i in range(0, numUsers):
        #     self.addUser(i)

        # targetFriendships = numUsers * avgFriendships
        # totalFriendships = 0
        # collisions = 0
        # while totalFriendships < targetFriendships:
        #     userID = random.randint(1, self.lastID)



if __name__ == '__main__':
    sg = SocialGraph()
    start_time = time.time()
    sg.populateGraph(20, 5)
    end_time = time.time()
    print (f"Runtime: {end_time - start_time} seconds")
    connections = sg.getAllSocialPaths(1)
    # print(connections)




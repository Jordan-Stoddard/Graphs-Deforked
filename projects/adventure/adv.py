from room import Room
from player import Player
from world import World
from room_graph import roomGraph
from util import Stack, Queue

import random


# Load world
world = World()
world.loadGraph(roomGraph)

# UNCOMMENT TO VIEW MAP
world.printRooms()
player = Player("Name", world.startingRoom)

traversalPath = []

room_id = player.currentRoom.id
exits = player.currentRoom.getExits()
# Initialize graph
exit_graph = {}
# Set starting room in graph.
exit_graph[room_id] = {i : '?' for i in exits}
unexplored = None


looping = True
while looping:
    # First time through the current room will be the starting room.
    current_room = exit_graph[room_id]
    # For every direction in the current room
    # If the current direction in the current room is '?':
        # travel that direction
        # add the room you travelled to to the exit_graph
        # if the room you travelled to's ID is already in the exit_graph, then pass
        # else create that room and place it in the exit_graph at the player.currentRoom.id
        # 4 if statements:
            # if the direction is ['direction'] then set the current room's previous room as that direction
    # else: see below
    for direction in current_room:
        try:
            if current_room[direction] == '?':
                player.travel(direction)
                traversalPath.append(f'{direction}')
                if player.currentRoom.id in exit_graph:
                    pass
                else:
                    exit_graph[player.currentRoom.id] = {i : '?' for i in player.currentRoom.getExits()}
                exit_graph[room_id][direction] = player.currentRoom.id
                if direction == 'n':
                    exit_graph[player.currentRoom.id]['s'] = room_id
                    room_id = player.currentRoom.id
                    break
                if direction == 's':
                    exit_graph[player.currentRoom.id]['n'] = room_id
                    room_id = player.currentRoom.id
                    break
                if direction == 'e':
                    exit_graph[player.currentRoom.id]['w'] = room_id
                    room_id = player.currentRoom.id
                    break
                if direction == 'w':
                    exit_graph[player.currentRoom.id]['e'] = room_id
                    room_id = player.currentRoom.id
                    break
        except KeyError:
            pass
        # If there are no '?' in current room it means there are no valid exits in this room.
            # check if there are any '?' anywhere in the exit_graph, it means there are still unexplored rooms.
            # Therefore we'll set unexplored to True
        if '?' not in current_room.values():
            for room in exit_graph:
                if '?' in exit_graph[room].values():
                    unexplored = True

            # If unexplored is true, and we're at a dead end, it means we need to find the shortest path
            # the below algorithm will find the shortest path back to a room that still has unexplored exits.
            if unexplored == True:
                visited = set()
                q = Queue()
                q.enqueue([player.currentRoom.id])

                while q.size() > 0:
                    path = q.dequeue()
                    v = path[-1]

                    if '?' in exit_graph[v].values():
                        break

                    if v not in visited:
                        visited.add(v)

                        for neighbor in exit_graph[v]:
                            if exit_graph[v][neighbor] not in visited:
                                path_copy = path.copy()
                                path_copy.append(exit_graph[v][neighbor])
                                q.enqueue(path_copy)
                # Once we're here, path will == a list of room ID's, this is the shortest path
                # back to the nearest room with an unexplored exit.
                # So for each room in the path, we want to do some things:
                    # if the current room == the player.currentRoom.id it means that we're already in that room,
                        # so we just pass.
                    # else:
                        # travel the directions listed in the path
                        # append that direction moved to the traversal path
                        # keep doing this until we get back to the nearest node with unexplored exits.
                unexplored = False
                for room in path:
                    if room == player.currentRoom.id:
                        pass
                    else:
                        if room in current_room.values():
                            # direction gets all the keys inside the current_room, and then finds the key value inside current_room
                            # where the current room id in the path matches the current_room's value at the room id.
                            direction = list(current_room.keys())[list(current_room.values()).index(room)]
                            player.travel(direction)
                            traversalPath.append(f'{direction}')
                            room_id = player.currentRoom.id
                            current_room = exit_graph[room_id]

            # if unexplored == False, it means every room has been explored
            # in which case we want to set looping to false, which causes us to break out of the loop
            # Because we've explored every room!
            else:
                looping = False



# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)

for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")

from room import Room
from player import Player
from world import World
from room_graph import roomGraph
from util import Stack, Queue

import random

# helper functions


# Load world
world = World()
world.loadGraph(roomGraph)

# UNCOMMENT TO VIEW MAP
# world.printRooms()
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
    current_room = exit_graph[room_id]
    temp_room = exit_graph[room_id]
    for direction in current_room:
        if current_room[direction] == '?':
            player.travel(direction)
            traversalPath.append(f'{direction}')
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
        if '?' not in current_room.values():
            for room in exit_graph:
                if '?' in exit_graph[room].values():
                    unexplored = True

            if unexplored == True:
                visited = set()
                q = Queue()
                q.enqueue([player.currentRoom.id])

                while q.size() > 0:
                    if '?' in temp_room.values():
                        break

                    path = q.dequeue()
                    v = path[-1]

                    if v not in visited:
                        visited.add(v)

                        for neighbor in exit_graph[v]:
                            if temp_room[neighbor] not in visited:
                                path_copy = path.copy()
                                path_copy.append(temp_room[neighbor])
                                q.enqueue(path_copy)
                                temp_room = exit_graph[temp_room[neighbor]]
                unexplored = False
                path = q.dequeue()
                for room in path:
                    if room == player.currentRoom.id:
                        pass
                    else:
                        if room in current_room.values():
                            direction = list(current_room.keys())[list(current_room.values()).index(room)]
                            player.travel(direction)
                            traversalPath.append(f'{direction}')
                            room_id = player.currentRoom.id
                            current_room = exit_graph[room_id]
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

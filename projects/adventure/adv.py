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



looping = True
while looping:
    current_room = exit_graph[room_id]
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
        else:
        








































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

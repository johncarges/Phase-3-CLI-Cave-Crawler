from PrettyPrint import PrettyPrintTree
from classes.World.Room import Room
import ipdb

room_nodes = []


class RoomNode:
    all = []

    def __init__(self, room):
        self.room = room
        self.value = room.type.replace("_", " ")
        self.name = room.name
        self.left = None
        self.straight = None
        self.right = None
        RoomNode.all.append(self)

    def add_child(self, child, direction):
        if direction == "left":
            self.left = child
        if direction == "straight":
            self.straight = child
        if direction == "right":
            self.right = child

    def __repr__(self):
        return (
            f"{self.name}"  # , left: {self.left}, straight: {self.straight}, right: {self.right}"
        )


def first_func(node):
    node_list = []
    if node == "?":
        return []
    if node.left:
        node_list.append(node.left)
    elif "left" in node.room.possible_directions():
        node_list.append("?")
    if node.straight:
        node_list.append(node.straight)
    elif "straight" in node.room.possible_directions():
        node_list.append("?")
    if node.right:
        node_list.append(node.right)
    elif "right" in node.room.possible_directions():
        node_list.append("?")

    return node_list


def second_func(node):
    if node == "?":
        return "?"
    else:
        return node.value


def print_map(current_room):
    print()
    RoomNode.all = []
    for room in Room.all:
        node = RoomNode(room)
        if room == current_room:
            node.value = "you"
    for node in RoomNode.all:
        for direction in ["left", "straight", "right"]:
            if direction in node.room.possible_directions():
                if new_room := node.room.adjacent_rooms[direction]:
                    new_child = [node for node in RoomNode.all if node.name == new_room.name][0]
                    node.add_child(new_child, direction)

    start_node = RoomNode.all[0]

    pt = PrettyPrintTree(first_func, second_func)
    pt(start_node, orientation=PrettyPrintTree.HORIZONTAL)
    # ipdb.set_trace()

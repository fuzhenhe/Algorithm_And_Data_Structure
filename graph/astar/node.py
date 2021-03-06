#!/usr/bin/env python3


class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent    # parent node
        self.position = position
        #self.position = (position[1], position[0])  # y, x
        self.distance_from_start = 0
        self.distance_to_end = 0
        self.cost = 0
        self.move = 0   # move counter

    def __str__(self):
        if self.position == None:
            return "None"
        else:
            return str(self.position)

    def __eq__(self, node):
        return self.position == node.position

    # unused
    def is_position(self, x, y):
        if self.position[0] == x and self.position[1] == y:
            return True
        return False

    def get_neighbor_positions(self, order=None):
        neighbors = []
        offsets = []
        if order == 0:
            offsets = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        elif order == 1:
            offsets = [(1,-1),(1,0),(0,-1),(1,1),(-1,-1),(0,1),(-1,0),(-1,1)]
        elif order == 2:
            offsets = [(1,-1),(1,0),(0,-1),(1,1),(-1,-1),(0,1),(-1,0),(-1,1)]
        elif order == 3:
            offsets = [(0,1),(0,-1),(-1,0),(1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
        elif order == 4:
            offsets = [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
        else:
            offsets = [(1,1),(1,0),(0,1),(1,-1),(-1,1),(0,-1),(-1,0),(-1,-1)]

        check_parent = True
        if self.parent is None:
            check_parent = False
        else:
            if self.parent.position is None:
                check_parent = False

        for offset in offsets:
            if offset[0] == 0 and offset[1] == 0:
                continue
            y = self.position[0] + offset[0]
            x = self.position[1] + offset[1]
            if check_parent:
                if self.parent.position[0] == y and self.parent.position[1] == x:
                    continue
            if x < 0 or y < 0:  # skip minus position
                continue
            neighbors.append((y,x))
        return neighbors

#!/usr/bin/python3
""" a method that determines if all boxes can be opened """


def canUnlockAll(boxes):
    """ a method that determines if all boxes can be opened """
    unlocked = {0}
    stack = [0]
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                stack.append(key)
    return len(unlocked) == len(boxes)

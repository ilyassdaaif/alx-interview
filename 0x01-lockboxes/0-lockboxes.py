#!/usr/bin/python3
"""
Module for the canUnlockAll function
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
    boxes (list of lists): A list of lists where each inner list represents a box
                           and contains keys to other boxes.
    
    Returns:
    bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    unlocked = set([0]) # Start with box 0 unlocked
    keys = set(boxes[0]) # Keys from the first box

    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(boxes[new_key])

    return len(unlocked) == n


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))

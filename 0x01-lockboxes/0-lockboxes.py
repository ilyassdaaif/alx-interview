#!/usr/bin/python3
"""Module that determines if all boxes can be opened"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
        boxes (list): A list of lists where each inner list represents a box.
    
    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    unlocked = set([0])
    keys = set(boxes[0])
    
    while keys:
        new_key = keys.pop()
        if new_key not in unlocked:
            if 0 <= new_key < n:
                unlocked.add(new_key)
                keys.update(set(boxes[new_key]) - unlocked)
    
    return len(unlocked) == n


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))

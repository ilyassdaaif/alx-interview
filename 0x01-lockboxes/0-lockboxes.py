#!/usr/bin/python3
<<<<<<< HEAD
""" a method that determines if all boxes can be opened """
=======

"""
This module contains the solution to the
Inteview question of lockboxes
"""
>>>>>>> 2a141a58134ea3aaf298a73257c5f20bf4c94640

from typing import List

<<<<<<< HEAD
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
=======

def canUnlockAll(boxes: List[List]) -> bool:
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing box and keys
    Returns:
        bool: True if all the boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list):
        raise TypeError('Boxes should be a list')

    key_list = [0]
    for key in key_list:
        for j in boxes[key]:
            if j not in key_list and j < len(boxes):
                key_list.append(j)
    for i in range(len(boxes)):
        if i not in key_list:
            return False
    return True
>>>>>>> 2a141a58134ea3aaf298a73257c5f20bf4c94640

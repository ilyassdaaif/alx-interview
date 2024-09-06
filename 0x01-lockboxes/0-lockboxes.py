#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes: A list of lists, where each inner list represents a box
               containing keys to other boxes.

    Returns:
        True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = set([0])  # Start with the first box unlocked
    queue = [0]  # Initialize a queue with the first box

    while queue:
        current_box = queue.pop(0)  # Get the first box from the queue

        for key in boxes[current_box]:
            if key < n and key not in visited:  # Check if the key is valid
                visited.add(key)  # Mark the box as visited
                queue.append(key)  # Add the box to the queue

    return len(visited) == n  # Check if all boxes have been visited

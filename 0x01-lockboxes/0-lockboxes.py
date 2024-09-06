#!/usr/bin/python3
"""
Module for the canUnlockAll function.
"""


def canUnlockAll(boxes):
    n = len(boxes)
    visited = set([0])  # Mark the first box as visited
    queue = [0]  # Start with the first box

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == n

#!/usr/bin/python3
"""
Lockboxes module
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    :param boxes: list of lists where each sublist contains keys to other boxes
    :return: True if all boxes can be opened, False otherwise
    """
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

# Code for testing the function
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False

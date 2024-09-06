#!/usr/bin/python3
"""
Module for the canUnlockAll function.
"""


def canUnlockAll(boxes):
    # Number of boxes
    n = len(boxes)
    
    # Set to track visited boxes
    visited = set()
    
    # Queue for BFS, start with box 0
    queue = [0]
    
    while queue:
        # Get the current box
        current_box = queue.pop(0)
        
        # If this box has already been visited, continue
        if current_box in visited:
            continue
        
        # Mark the current box as visited
        visited.add(current_box)
        
        # Add all keys in the current box to the queue
        for key in boxes[current_box]:
            if key not in visited:
                queue.append(key)
    
    # Check if we have visited all boxes
    return len(visited) == n

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False

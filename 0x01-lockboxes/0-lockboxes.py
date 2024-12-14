#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
        boxes (list of lists): A list where each index represents a box,
                                and the value is a list of keys to other boxes.
    
    Returns:
        bool: True if all boxes can be opened, False otherwise
    """
    # If there are no boxes or only the first box, return True
    if not boxes:
        return False
    
    # Total number of boxes
    n = len(boxes)
    
    # Set to keep track of opened boxes
    unlocked = set([0])  # First box is always unlocked
    
    # Queue to process keys
    keys_to_process = list(boxes[0])
    
    while keys_to_process:
        # Get a key
        key = keys_to_process.pop(0)
        
        # If the key is valid and the box hasn't been opened
        if 0 <= key < n and key not in unlocked:
            # Mark the box as opened
            unlocked.add(key)
            
            # Add new keys from this box
            keys_to_process.extend(boxes[key])
    
    # Check if the number of opened boxes equals total number of boxes
    return len(unlocked) == n

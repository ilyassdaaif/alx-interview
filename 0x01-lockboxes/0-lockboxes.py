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
    if not boxes:
        return False
    
    n = len(boxes)
    
    opened = set([0])  
    
    keys_to_process = list(boxes[0])
    
    while keys_to_process:
        key = keys_to_process.pop(0)
        
        if 0 <= key < n and key not in opened:
            opened.add(key)
            
            keys_to_process.extend(boxes[key])
    
    return len(opened) == n

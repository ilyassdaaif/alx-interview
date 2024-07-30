#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = set()
    keys = [0]

    while keys:
        current_key = keys.pop()
        if current_key not in unlocked:
            unlocked.add(current_key)
            for key in boxes[current_key]:
                if key not in unlocked and key < n:
                    keys.append(key)
    
    return len(unlocked) == n

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False

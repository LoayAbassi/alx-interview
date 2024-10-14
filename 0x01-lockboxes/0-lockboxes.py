#!/usr/bin/python3
"""
contains unlockbox solved
"""


def canUnlockAll(boxes):
    """
    returns unlockabilty of boxes (boolean)
    boxes : list[list(int)]
    """
    pending = [0]
    keys = {0}

    while pending:
        box = pending.pop()
        for key in boxes[box]:
            if key not in keys and key < len(boxes):
                keys.add(key)
                pending.append(key)

    return len(keys) == len(boxes)

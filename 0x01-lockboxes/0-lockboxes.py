#!/usr/bin/python3
"""
0. lock boxes
"""


def canUnlockAll(boxes):
    """unlock all function"""

    listKey = [0]
    skippedKey = []
    for i in range(len(boxes)):
        if i == 0:
            for k in boxes[i]:

                listKey.append(k)

        if i in listKey:
            for k in boxes[i]:

                listKey.append(k)

        if i not in listKey:
            skippedKey.append(i)

    for i in skippedKey:
        if i in listKey:

            for k in boxes[i]:

                listKey.append(k)

    value = True
    for i in range(len(boxes)):

        if i not in listKey:
            value = False

    return value
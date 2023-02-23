#!/usr/bin/python3
""" Rain trap """


def rain(walls):
    n = len(walls)
    if n == 0:
        return 0

    left = 0
    right = n-1
    left_side = 0
    right_side = 0
    water = 0

    while left < right:
        if walls[left] < walls[right]:
            if walls[left] >= left_side:
                left_side = walls[left]
            else:
                water += left_side - walls[left]
            left += 1
        else:
            if walls[right] >= right_side:
                right_side = walls[right]
            else:
                water += right_side - walls[right]
            right -= 1

    return water

#!/usr/bin/python3
""" Rain trap """


def rain(walls):
  
    res = 0
    for i in range(1, n - 1):
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])
        right = arr[i]
        for j in range(i + 1, n):
            right = max(right, arr[j])
        res = res + (min(left, right) - arr[i])
    return res

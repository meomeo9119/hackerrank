#!/bin/python3
import sys

def super_reduced_string(s):
    # Complete this function
    stack = []
    for i in range(len(s)):
        if not stack or s[i] != stack[-1]:
            stack += [s[i]]
        else:
            stack.pop()
    return ''.join(stack)

s = input().strip()
result = super_reduced_string(s)
if result:
    print(result)
else:
    print("Empty String")

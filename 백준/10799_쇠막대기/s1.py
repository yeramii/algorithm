"""
Pass - 31900KB 68ms
"""
import sys
sys.stdin = open("input.txt")

tmp = input()
stack = [0] * len(tmp)
top = -1
ans = 0
for i, c in enumerate(tmp):
    if c == "(":
        top += 1
        stack[top] = c
    elif c == ")":
        if tmp[i-1] == "(":
            ans += top
        else:
            ans += 1
        top -= 1
print(ans)
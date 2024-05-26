"""
Pass - 31120KB 40ms
"""
import sys
sys.stdin = open("input.txt")

lst = [-1 for _ in range(26)]
for i, s in enumerate(input()):
    tmp = ord(s) - 97
    if lst[tmp] == -1:
        lst[tmp] = i
print(' '.join(map(str, lst)))
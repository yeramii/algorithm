"""
Pass - 31120KB 40ms
"""
import sys
sys.stdin = open("input.txt")

A, P = map(int, input().split())
lst = [A]
n = A
while True:
    nn = 0
    for c in str(n):
        nn += int(c) ** P
    if nn in lst:
        break
    lst.append(nn)
    n = nn
print(lst.index(nn))
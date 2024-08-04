"""
Pass - PyPy3 : 213364KB 9068ms
Fail - Python3 : 시간 초과
"""
import sys
sys.stdin = open("input.txt")
from collections import deque

def register(c, n):
    if c == "D":
        return (2 * n) % 10000
    elif c == "S":
        return (n + 9999) % 10000
    elif c == "L":
        return (10 * n) % 10000 + (10 * n) // 10000
    else:
        return n // 10 + (n % 10) * 1000

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10000
    visited[A] = 1
    q = deque([])
    q.append((A, ""))
    while q:
        v, cmds = q.popleft()
        if v == B:
            print(cmds)
            break
        for s in "DSLR":
            tmp = register(s, v)
            if not visited[tmp]:
                visited[tmp] = 1
                q.append((tmp, cmds+s))

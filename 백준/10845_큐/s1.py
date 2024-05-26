"""
Pass
    1) 빈 list에 append(), pop(0) 사용 - 31120KB, 48ms
    2) deque 사용 - 34044KB 72ms
    3) 일정 크기 list에 front/rear 사용 (s2.py) - 31120KB 52ms

- input() 대신 sys.stdin.readline() 사용 !!
"""
import sys
from collections import deque
sys.stdin = open("input.txt")

N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    tmp = sys.stdin.readline().split()
    if tmp[0] == "push":
        q.append(tmp[1])
    elif tmp[0] == "pop":
        if not len(q):
            print(-1)
        else:
            print(q.popleft())
    elif tmp[0] == "size":
        print(len(q))
    elif tmp[0] == "empty":
        if len(q):
            print(0)
        else:
            print(1)
    elif tmp[0] == "front":
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif tmp[0] == "back":
        if len(q):
            print(q[-1])
        else:
            print(-1)
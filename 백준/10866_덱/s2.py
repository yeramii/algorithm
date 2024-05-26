from collections import deque
import sys
sys.stdin = open("input.txt")

N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    tmp = sys.stdin.readline().split()
    if tmp[0] == "push_front":
        q.appendleft(tmp[1])
    elif tmp[0] == "push_back":
        q.append(tmp[1])
    elif tmp[0] == "pop_front":
        if not len(q):
            print(-1)
        else:
            print(q.popleft())
    elif tmp[0] == "pop_back":
        if not len(q):
            print(-1)
        else:
            print(q.pop())
    elif tmp[0] == "size":
        print(len(q))
    elif tmp[0] == "empty":
        if not len(q):
            print(1)
        else:
            print(0)
    elif tmp[0] == "front":
        if not len(q):
            print(-1)
        else:
            print(q[0])
    elif tmp[0] == "back":
        if not len(q):
            print(-1)
        else:
            print(q[-1])

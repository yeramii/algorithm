"""
Pass - 31120KB 52ms
    선형큐 사용
"""
import sys
sys.stdin = open("input.txt")

N = int(sys.stdin.readline())
q = [0 for _ in range(N)]
front = -1
rear = -1
for _ in range(N):
    tmp = sys.stdin.readline().split()
    if tmp[0] == "push":
        rear += 1
        q[rear] = tmp[1]
    elif tmp[0] == "pop":
        if front == rear:
            print(-1)
        else:
            front += 1
            print(q[front])
    elif tmp[0] == "size":
        print(rear - front)
    elif tmp[0] == "empty":
        if front != rear:
            print(0)
        else:
            print(1)
    elif tmp[0] == "front":
        if front != rear:
            print(q[front+1])
        else:
            print(-1)
    elif tmp[0] == "back":
        if front != rear:
            print(q[rear])
        else:
            print(-1)
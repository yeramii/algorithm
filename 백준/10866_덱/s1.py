"""
Pass
    1) 일정 크기 list에 front/rear 사용 - 31120KB 48ms
    2) deque() 사용 (s2.py) - 34072KB 76ms
"""
import sys
sys.stdin = open("input.txt")

N = int(sys.stdin.readline())
q = [0 for _ in range(N)]
front = 0
rear = 0
for _ in range(N):
    tmp = sys.stdin.readline().split()
    if tmp[0] == "push_front":
        q[front] = tmp[1]
        front = (front - 1 + N) % N
    elif tmp[0] == "push_back":
        rear = (rear + 1) % N
        q[rear] = tmp[1]
    elif tmp[0] == "pop_front":
        if front == rear:
            print(-1)
        else:
            front = (front + 1) % N
            print(q[front])
    elif tmp[0] == "pop_back":
        if front == rear:
            print(-1)
        else:
            print(q[rear])
            rear = (rear - 1 + N) % N
    elif tmp[0] == "size":
        print((rear - front + N) % N)
    elif tmp[0] == "empty":
        if front == rear:
            print(1)
        else:
            print(0)
    elif tmp[0] == "front":
        if front == rear:
            print(-1)
        else:
            print(q[(front+1) % N])
    elif tmp[0] == "back":
        if front == rear:
            print(-1)
        else:
            print(q[rear])

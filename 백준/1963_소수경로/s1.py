import sys
sys.stdin = open("input.txt")
from collections import deque

T = int(input())
prime = [True] * 10001
for i in range(2, 100):
    if prime[i] == False:
        continue
    prime[i] = True
    for j in range(2*i, 10000, i):
        prime[j] = False

for _ in range(T):
    start, end = map(int, input().split())
    visited = [0] * 10001
    visited[start] = 1
    q = deque([])
    q.append((str(start), 0))
    is_done = False
    while q:
        v, cnt = q.popleft()
        if v == str(end):
            is_done = True
            break
        for i in range(4):
            for j in range(10):
                nxt = str(v)[:i] + str(j) + str(v)[i+1:]
                if int(nxt) > 999 and prime[int(nxt)] and not visited[int(nxt)]:
                    visited[int(nxt)] = 1
                    q.append((nxt, cnt+1))
    if is_done:
        print(cnt)
    else:
        print('impossible')
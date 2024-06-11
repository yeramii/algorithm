import sys
sys.stdin = open("input.txt")
from collections import deque

R, C = map(int, input().split())
arr = []
for _ in range(R):
    tmp = []
    for c in input():
        tmp.append(int(c))
    arr.append(tmp)

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

q = deque([(0, 0)])
while q:
    (r, c) = q.popleft()
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if rr in range(R) and cc in range(C) and arr[rr][cc] == 1:
            arr[rr][cc] = arr[r][c] + 1
            q.append((rr, cc))
print(arr[R-1][C-1])
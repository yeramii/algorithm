"""
Pass - 41776KB 1120ms

bfs
"""
import sys
sys.stdin = open("input.txt")
from collections import deque

R, C = map(int, input().split())
arr = []
ans = []
target = [0, 0]
for r in range(R):
    tmp = list(map(int, input().split()))
    if 2 in tmp:
        target[0] = r
        target[1] = tmp.index(2)
    arr.append(tmp)
    ans.append(list(map(lambda x: -x, tmp)))
ans[target[0]][target[1]] = 0
visited = [[0]*C for _ in range(R)]
visited[target[0]][target[1]] = 1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
q = deque([])
q.append([target[0], target[1], 0])

while q:
    r, c, dist = q.popleft()
    for k in range(4):
        rr = r + dr[k]
        cc = c + dc[k]
        if rr not in range(R) or cc not in range(C) or visited[rr][cc]:
            continue
        if arr[rr][cc] != 1:
            continue
        if ans[rr][cc] == -1 or ans[rr][cc] > dist:
            ans[rr][cc] = dist+1
            q.append([rr, cc, dist+1])
            visited[rr][cc] = 1
for line in ans:
    for c in line:
        print(c, end=' ')
    print()
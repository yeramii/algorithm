
import sys
sys.stdin = open("input.txt")
from collections import deque
from copy import deepcopy

arr = []
for r in range(3):
    tmp = list(map(int, input().split()))
    for c in range(3):
        if tmp[c] == 0:
            hole = (r, c)
    arr.append(tmp)
ans = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
q = deque([])
q.append((arr, 0, hole))
visited = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
while q:
    a, c, h = q.popleft()
    if a == ans:
        break
    # 상 하 좌 우 움직여 보면서 visited에 없으면 넣고, q에도 cnt랑 같이 넣음
    for k in range(4):
        rr = h[0] + dr[k]
        cc = h[1] + dc[k]
        if rr in range(3) and cc in range(3):
            tmp = deepcopy(a)
            tmp[rr][cc], tmp[h[0]][h[1]] = tmp[h[0]][h[1]], tmp[rr][cc]
            if tmp not in visited:
                visited.append(deepcopy(tmp))
                q.append((tmp, c+1, (rr, cc)))

if a == ans:
    print(c)
else:
    print(-1)

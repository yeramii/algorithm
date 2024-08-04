"""
Pass - 35304KB 276ms

BFS
- 빨리 구하는 것이 장땡이므로 (cnt가 적은 것), BFS를 써야 함
- 처음엔 DFS를 썼는데 함수 호출이 많아서인지 메모리 초과 발생
"""
import sys
sys.stdin = open("input.txt")
from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001
ans = abs(N-K)
q = deque([])
q.append([N, 0])

while q:
    x, cnt = q.popleft()
    if x == K:
        ans = cnt
        break
    if 2*x in range(len(visited)) and not visited[2*x]:
        visited[2*x] = 1
        q.append([2*x, cnt+1])
    if x+1 in range(len(visited)) and not visited[x+1]:
        visited[x+1] = 1
        q.append([x+1, cnt+1])
    if x-1 in range(len(visited)) and not visited[x-1]:
        visited[x-1] = 1
        q.append([x-1, cnt+1])
print(ans)

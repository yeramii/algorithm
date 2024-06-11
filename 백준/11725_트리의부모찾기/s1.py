import sys
sys.stdin = open("input.txt")
from collections import deque

N = int(input())
conn = [[] for _ in range(N+1)]
child = [[] for _ in range(N+1)]
par = [0] * (N+1)
for _ in range(N-1):
    n, m = map(int, input().split())
    conn[n].append(m)
    conn[m].append(n)
q = deque([1])
while q:
    p = q.popleft()
    for c in conn[p]:
        if par[p] == c: continue
        par[c] = p
        child[p].append(c)
        q.append(c)
for c in par[2:]:
    print(c)

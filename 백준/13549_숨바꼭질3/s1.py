"""
Pass
1) 최소힙    34996KB 132ms (*2, -1, +1 순서)
                    140ms (*2, +1, -1 순서)
                    180ms (N과 K 크기 비교하는 if문 없앴을 때)
2) 우선순위큐 34220KB 120ms (*2, -1, +1 순서)
"""
import sys
sys.stdin = open("input.txt")


# 1) heapq (최소 힙)
def min_heap(start, end):
    from heapq import heappop, heappush

    q = []
    heappush(q, (0, start))

    visited = [0] * 100001
    visited[start] = 1
    while q:
        cnt, node = heappop(q)
        if node == end:
            return cnt
        if 2 * node in range(100001) and not visited[2*node]:
            visited[2*node] = 1
            heappush(q, (cnt, 2*node))
        if node+1 in range(100001) and not visited[node+1]:
            visited[node+1] = 1
            heappush(q, (cnt+1, node+1))
        if node-1 in range(100001) and not visited[node-1]:
            visited[node-1] = 1
            heappush(q, (cnt+1, node-1))

# 2) deque (우선순위 큐)
def priority_q(start, end):
    from collections import deque

    q = deque()
    q.append(start)

    visited = [0] * 100001
    visited[start] = 1
    cnt = [0] * 100001
    while q:
        node = q.popleft()
        if node == end:
            return cnt[node]
        if 2*node in range(100001) and not visited[2*node]:
            q.appendleft(2*node)
            cnt[2*node] = cnt[node]
            visited[2*node] = 1
        if node-1 in range(100001) and not visited[node-1]:
            q.append(node-1)
            cnt[node-1] = cnt[node]+1
            visited[node-1] = 1
        if node+1 in range(100001) and not visited[node+1]:
            q.append(node+1)
            cnt[node+1] = cnt[node]+1
            visited[node+1] = 1


N, K = map(int, input().split())
if N >= K:
    print(N - K)
else:
    # ans = min_heap(N, K)
    ans = priority_q(N, K)
    print(ans)

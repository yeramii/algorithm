"""
Pass
1) merge sort - 187264KB 2416ms
2) 내장 sort() - 304400KB 1160ms
3) 내장 heapq - 189352KB 3108ms
"""
import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

### 1) merge sort
ans = []
a = 0
b = 0
while a < N and b < M:
    if A[a] <= B[b]:
        ans.append(A[a])
        a += 1
    else:
        ans.append(B[b])
        b += 1
while a < N:
    ans.append(A[a])
    a += 1
while b < M:
    ans.append(B[b])
    b += 1
for n in ans:
    print(n, end=' ')

### 2) sort()
C = A + B
C.sort()
print(' '.join(map(str, C)))

### 3) heapq
import heapq
heapq.heapify(A)
for b in B:
    heapq.heappush(A, b)
for _ in range(N+M):
    print(heapq.heappop(A), end=' ')

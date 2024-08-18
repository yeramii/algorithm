import sys
sys.stdin = open("input.txt")
from bisect import bisect_left, bisect_right

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

accA, accB = [], []
for i in range(n):
    for j in range(i+1, n+1):
        accA.append(sum(A[i:j]))
for i in range(m):
    for j in range(i+1, m+1):
        accB.append(sum(B[i:j]))
accA.sort()
accB.sort()

ans = 0
for i in range(len(accA)):
    diff = T - accA[i]
    left = bisect_left(accB, diff)
    right = bisect_right(accB, diff)
    ans += right - left
print(ans)

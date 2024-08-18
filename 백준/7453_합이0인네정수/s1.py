"""
Pass - PyPy3

s1. 689120KB 7012ms
    : meet in the middle (two pointers)
    => 알고리즘을 활용한 풀이 (s1) 가 내장함수들을 활용한 풀이 (s2)보다 좋은 성능
s2. 1532944KB 9432ms
    : from collections import Counter
"""
import sys
sys.stdin = open("input.txt")

n = int(sys.stdin.readline())
A, B, C, D = [], [], [], []
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    A.append(tmp[0])
    B.append(tmp[1])
    C.append(tmp[2])
    D.append(tmp[3])

inc, dec = [], []
for i in range(n):
    for j in range(n):
        inc.append(A[i] + B[j])
        dec.append(C[i] + D[j])
inc.sort()
dec.sort(reverse=True)

cnt = 0
i, d = 0, 0
while i < len(inc) and d < len(dec):
    if inc[i] + dec[d] > 0:
        d += 1
    elif inc[i] + dec[d] < 0:
        i += 1
    else:
        ii, dd = i, d
        while ii < len(inc) and inc[ii] == inc[i]:
            ii += 1
        while dd < len(dec) and dec[dd] == dec[d]:
            dd += 1
        cnt += (ii-i) * (dd-d)
        i, d = ii, dd
print(cnt)
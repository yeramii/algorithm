"""
Pass - 93620KB 1480ms

99%에서 index error가 나서 lst가 생성되지 않는 경우를 추가
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
# 1. N 이하 prime 구해서 별도 lst 생성
primes = [False, False] + [True] * (N-1)
lst = []
for i in range(2, N+1):
    if primes[i]:
        lst.append(i)
        for j in range(2*i, N+1, i):
            primes[j] = False
# 2. lst의 부분합 구해서 N이 되는지 확인
if lst:
    tmp = lst[0]
    s, e = 0, 0
    cnt = 0
    while True:
        if tmp >= N:
            if tmp == N:
                cnt += 1
            tmp -= lst[s]
            s += 1
            if s >= len(lst): break
            if s > e: e = s
        else:
            e += 1
            if e >= len(lst): break
            tmp += lst[e]
    print(cnt)
else:
    print(0)

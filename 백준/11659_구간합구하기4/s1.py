"""
Pass - 41144KB 276ms

다른 사람 풀이 참고 - "누적 합 구하기" (cumulative sum)
"""
import sys
sys.stdin = open("input.txt")

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
csum = num[:]
for i in range(1, N):
    csum[i] += csum[i-1]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(csum[j-1] - csum[i-2] if i > 1 else csum[j-1])
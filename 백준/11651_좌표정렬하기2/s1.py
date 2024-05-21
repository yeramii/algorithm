"""
Pass - 44580KB 324ms

이전 문제 (11650)와 동일한 방법인데 순서만 바뀜
"""
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    a, b = list(map(int, sys.stdin.readline().split()))
    arr.append((b, a))
arr.sort()
for i in range(N):
    print(arr[i][1], arr[i][0])
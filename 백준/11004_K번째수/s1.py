"""
Pass - 622164KB 3780ms
"""
import sys
sys.stdin = open("input.txt")

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
print(A[K-1])
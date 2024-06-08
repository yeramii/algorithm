"""
Pass - 31120KB 2176ms
"""
import sys
sys.stdin = open("input.txt")

A, B = map(int, input().split())
while B > 0:
    A, B = B, A % B
for _ in range(A):
    print("1", end="")
"""
Pass - 31252KB 44ms

ord, chr 안 쓰고도 할 수 있음 -> s2.py
"""
import sys
sys.stdin = open("input.txt")

N, B = map(int, input().split())
lst = []
while True:
    if N < B:
        break
    lst.append(N % B)
    N //= B
lst.append(N)
for n in lst[::-1]:
    if n >= 10:
        print(chr(n+55), end="")    # ord("A") = 65
    else:
        print(n, end="")


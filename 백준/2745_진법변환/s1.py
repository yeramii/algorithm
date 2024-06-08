"""
Pass - 31120KB 40ms
"""
import sys
sys.stdin = open("input.txt")

N, B = list(input().split())
tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = 0
for idx, char in enumerate(N[::-1]):
    ans += tmp.index(char) * (int(B) ** idx)
print(ans)
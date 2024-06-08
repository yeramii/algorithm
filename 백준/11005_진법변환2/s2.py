"""
Pass - 31252KB 44ms
"""
import sys
sys.stdin = open("input.txt")

tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = map(int, input().split())
ans = ''
while N > 0:
    ans += str(tmp[N % B])
    N //= B
print(ans[::-1])
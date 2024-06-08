"""
Pass - 31120KB 48ms
"""
import sys
sys.stdin = open("input.txt")

A, B = map(int, input().split())
m = int(input())
a_lst = list(map(int, input().split()))
num = 0
for i, c in enumerate(a_lst[::-1]):
    num += c * (A ** i)
ans = []
while True:
    ans.append(str(num % B))
    num //= B
    if num < B:
        ans.append(str(num))
        break
print(" ".join(ans[::-1]))
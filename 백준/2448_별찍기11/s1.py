"""
Pass - 90744KB 96ms
"""
import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10 ** 6)

N = int(input())

def star(n):    # n = 층 수
    if n == 0:
        return "*"
    if n == 1:
        return ["  *  ", " * * ", "*****"]
    stars = star(n-1)
    ans = []
    for s in stars:
        ans.append(' '*len(stars) + s + ' '*len(stars))
    for s in stars:
        ans.append(s + ' ' + s)
    return ans

def find_k(n):
    cnt = 1
    while n != 1:
        cnt += 1
        n //= 2
    return cnt

ans = star(find_k(N//3))
print('\n'.join(ans))
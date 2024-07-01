"""
Pass - 45220KB 56ms

다른 사람의 풀이 참고
"""
import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10 ** 6)

N = int(input())

def star(n):
    if n == 1:
        return ['*']
    stars = star(n // 3)
    ans = []
    for s in stars:
        ans.append(s*3)
    for s in stars:
        ans.append(s + ' ' * (n//3) + s)
    for s in stars:
        ans.append(s*3)
    return ans

ans = star(N)
print('\n'.join(ans))

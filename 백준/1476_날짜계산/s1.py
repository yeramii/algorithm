"""
Pass - 31120KB 32ms
"""
import sys
sys.stdin = open("input.txt")

E, S, M = map(int, input().split())
ans = S
while True:
    if ans%15 == E%15 and ans%19 == M%19:
        break
    ans += 28
print(ans)
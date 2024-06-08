"""
Pass - 31120KB 32ms
"""
import sys
sys.stdin = open("input.txt")

n = int(input())
ans = ''
q = n
idx = 0
while True:
    idx += 1
    r = q % -2
    q = q // -2
    if r == -1:
        q += 1
        r = 1
    ans += str(r)
    if q in [0, 1]:
        if q == 1:
            ans += str(q)
        break
print(ans[::-1])
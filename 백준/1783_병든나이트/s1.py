"""
Pass - 31120KB 44ms

너무 많은 분기
"""
import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
if N == 1:
    cnt = 1
elif N == 2:
    if M < 3:
        cnt = 1
    elif M < 5:
        cnt = 2
    elif M < 7:
        cnt = 3
    else:
        cnt = 4
else:
    if M < 2:
        cnt = 1
    elif M < 3:
        cnt = 2
    elif M < 4:
        cnt = 3
    elif M < 7:
        cnt = 4
    else:
        cnt = M-2
print(cnt)

"""
s1) Pass - 31120KB 480ms
s2) Fail - 반례

s2로 복잡도를 확 줄이려 했는데, 반례가 너무 많아서 그냥 완전 탐색으로 품
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
M = int(input())
safe = [True] * 10
if M:
    broken = sorted(list(map(int, input().split())), reverse=True)
    for b in broken:
        safe[b] = False

def validate(num):
    for n in str(num):
        if not safe[int(n)]:
            break
    else:
        return True
    return False

if N == 100:
    print(0)
else:
    is_done = False
    if validate(N):
        is_done = True
        print(min(len(str(N)), abs(100-N)))
    if not is_done:
        tmp = abs(100 - N)
        ans = abs(100 - N)
        cnt = 0
        tmp_high = N
        tmp_low = N
        while cnt <= tmp:
            tmp_high += 1
            tmp_low -= 1
            cnt += 1
            if validate(tmp_high):
                ans = cnt + len(str(tmp_high))
                if tmp_low >= 0 and validate(tmp_low):
                    ans = min(ans, cnt + len(str(tmp_low)))
                break
            if tmp_low >= 0 and validate(tmp_low):
                ans = cnt + len(str(tmp_low))
                break
        tmp = min(ans, tmp)
        print(tmp)
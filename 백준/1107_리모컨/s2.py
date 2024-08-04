import sys
sys.stdin = open("input.txt")

N = int(input())
M = int(input())
safe = [True] * 10
if M:
    broken = sorted(list(map(int, input().split())), reverse=True)
    for b in broken:
        safe[b] = False

if N == 100:
    print(0)
else:
    tmp_low = ""
    tmp_high = ""
    is_low = False
    is_high = False
    for n in str(N):
        if not is_low:
            i = int(n)
        else:
            i = 9
        if not is_high:
            j = int(n)
        else:
            j = 0
        while i >= 0:
            if safe[i]:
                tmp_low += str(i)
                break
            else:
                i -= 1
                is_low = True
        while j < 10:
            if safe[j]:
                tmp_high += str(j)
                break
            else:
                j += 1
                is_high = True
    # 아래 반례에 걸림
    """
    2229
    6
    4 5 6 7 8 9
    """
    if not is_low and tmp_low:
        idx = 1
        is_done = False
        rev_low = tmp_low
        while idx <= len(tmp_low):
            if is_done:
                break
            n = int(rev_low[-idx])
            for i in range(1, 10):
                if safe[(n+i)%10]:
                    if n > (n+i)%10:
                        is_done = True
                    rev_low[-idx] = str((n+i)%10)
                    break
            idx += 1
        if abs(int(rev_low)-N) < abs(int(tmp_low)-N):
            tmp_low = rev_low

    tmp = abs(100-N)
    if tmp_low:
        tmp = min(abs(int(tmp_low)-N) + len(tmp_low), tmp)
    if tmp_high:
        tmp = min(abs(int(tmp_high)-N) + len(tmp_high), tmp)
    print(tmp)
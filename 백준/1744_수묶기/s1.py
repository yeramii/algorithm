"""
Pass -

반례를 못 찾아서 계속 해멤
- 반례 : 모두 양수인 경우
     -> 2번째 while 문으론 가지 않아야 함. (양수끼리 곱해야 하니까)
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
ser = [int(input()) for _ in range(N)]
ser.sort(reverse=True)
if 0 in ser:
    zero_at = ser.index(0)
else:
    zero_at = N
    for i in range(N):
        if ser[i] < 0:
            zero_at = i
            break
# 음수와 0은 서로 묶고, 1은 묶지 않고, 양수는 묶는다.
ans = 0
i = 0
while i < zero_at:
    if i+1 < zero_at and ser[i+1] != 1:
        ans += ser[i] * ser[i+1]
        i += 2
    else:
        ans += ser[i]
        i += 1
j = N-1
while j >= zero_at:
    if j-1 >= zero_at and ser[j-1] <= 0:
        ans += ser[j] * ser[j-1]
        j -= 2
    else:
        ans += ser[j]
        j -= 1
print(ans)
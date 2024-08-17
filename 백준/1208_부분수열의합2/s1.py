"""
meet in the middle (two pointer)
: 감소 배열, 증가 배열을 만들고 합이 크면 감소 배열 idx+1, 합이 작으면 증가 배열 idx+1

bisect : 이진 탐색을 쉽게 구현하게끔 해주는 함수
from bisect import bisect_left, bisect_right
    bisect_right(arr, n) : arr에서 n보다 큰 수가 있는 첫 번째 idx
    bisect_left(arr, n) : arr에서 n보다 크거나 같은 수가 있는 첫 번째 idx

s1. 211660KB 700ms
    1) Pass - while
    2) Fail - for & if
    => 시간 복잡도 측면에서 뭐가 나은거지?

s2. 212824KB 1060ms
    : s1과 같이 meet in the middle인데, bisect를 사용
"""
import sys
sys.stdin = open("input.txt")
from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))
inc = []
dec = []
tmp = nums[:len(nums)//2]
for i in range(len(tmp)+1):
    for comb in combinations(tmp, i):
        inc.append(sum(comb))
tmp = nums[len(nums)//2:]
for i in range(len(tmp)+1):
    for comb in combinations(tmp, i):
        dec.append(sum(comb))
inc.sort()
dec.sort(reverse=True)

i, d = 0, 0
ans = 0
while i < len(inc) and d < len(dec):
    if inc[i] + dec[d] > S:
        d += 1
    elif inc[i] + dec[d] < S:
        i += 1
    else:
        # 1) Pass
        ii, dd = i, d
        while ii < len(inc) and inc[ii] == inc[i]:
            ii += 1
        while dd < len(dec) and dec[dd] == dec[d]:
            dd += 1
        ans += (ii-i) * (dd-d)
        i, d = ii, dd
        # 2) Fail (time over)
        # cnt_i, cnt_d = 0, 0
        # for ii in range(i, len(inc)):
        #     if inc[ii] == inc[i]:
        #         cnt_i += 1
        #     else:
        #         i = ii
        #         break
        # for dd in range(d, len(dec)):
        #     if dec[dd] == dec[d]:
        #         cnt_d += 1
        #     else:
        #         d = dd
        #         break
        # ans += cnt_i * cnt_d

print(ans-1 if not S else ans)
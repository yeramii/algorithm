'''
Python3 - Pass

[시간단축법]
- 입력받을 때 input() 대신 sys.stdin.readline() 사용
- 대신 제출할 때 import sys 생략하면 안 됨!
'''

import sys
sys.stdin = open('input3.txt')

from collections import Counter

N = int(input())    # 500,000 이하
nums = [0] * N
for idx in range(N):
    nums[idx] = int(sys.stdin.readline())

nums.sort()
print(round(sum(nums)/N))   # 산술평균
print(nums[N//2])           # 중앙값

cnt = Counter(nums).most_common(2)  # 빈도수가 높은 숫자 2개를 가져온다.
if N > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(nums[-1]-nums[0])     # 범위
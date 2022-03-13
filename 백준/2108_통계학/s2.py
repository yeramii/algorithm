'''
Python3 - Fail(시간 초과)
PyPy3 - Pass(왜지?)
'''

import sys
sys.stdin = open('input3.txt')

from collections import Counter

N = int(input())    # 500,000 이하
nums = [0] * N
for idx in range(N):
    nums[idx] = int(input())

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

'''
class collections.Counter([iterable-or-mapping])
- counter는 해시 가능한 객체를 세기 위한 dict 서브 클래스
- 요소가 key로 저장되고, 개수가 value로 저장되는 collection

- elements() : 개수만큼 반복되는 요소에 대한 iterator 반환
- most_common([n]) : n개의 가장 흔한 요소와 그 개수를 가장 흔한 것부터 가장 적은 것 순으로 나열한 list 반환
- subtract([iterable-or-mapping]) : iterable이나 다른 mapping으로부터 온 요소들을 뺀다.
- total() : 모든 value의 sum

'''
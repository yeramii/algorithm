'''
Fail(시간 초과)
- 빈도수를 하나하나 세서 초과인듯 하다
'''
import sys
sys.stdin = open('input3.txt')

N = int(input())    # 500,000 이하
nums = [0] * N
for idx in range(N):
    nums[idx] = int(input())

# 정렬
nums.sort()

# 빈도수
often_cnt = 1
often_lst = []
ans = 0
for num in nums:
    cnt = nums.count(num)
    if cnt > 1 and cnt == often_cnt and often_lst[-1] != num:
        often_lst.append(num)
    elif cnt > often_cnt:
        often_lst = [num]
        often_cnt = cnt
if often_lst == []:
    if N >= 2:
        ans = nums[1]
    else:
        ans = nums[0]
elif len(often_lst) >= 2:
    ans = often_lst[1]

print(round(sum(nums)/N))   # 산술평균
print(nums[N//2])           # 중앙값
print(ans)                  # 최빈값
print(nums[-1]-nums[0])     # 범위

'''
[통계학]
1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이
'''
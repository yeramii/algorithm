"""
1) bubble sort - Fail (시간 초과)
2) merge sort - Pass (90168KB 2164ms)
3) segment tree - ?
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
A = list(map(int, input().split()))


### 1) bubble sort - Fail (시간 초과)
# ans = 0
# end = N-1
# while end > 0:
#     last = 0
#     for i in range(end):
#         if A[i] > A[i+1]:
#             A[i], A[i+1] = A[i+1], A[i]
#             ans += 1
#             last = i
#     end = last
# print(ans)

### 2) merge sort
def merge(left, right):
    global ans
    i, j = 0, 0
    tmp = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            tmp.append(right[j])
            j += 1
            ans += len(left) - i
        else:
            tmp.append(left[i])
            i += 1
    if i != len(left):
        tmp.extend(left[i:])
    elif j != len(right):
        tmp.extend(right[j:])
    return tmp

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)

ans = 0
A = merge_sort(A)
print(ans)

### 3) segment tree
# 참고 : https://velog.io/@babnbabn/1517%EB%B2%88-%EB%B2%84%EB%B8%94-%EC%86%8C%ED%8A%B8-Python
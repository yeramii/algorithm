"""
Pass
    - PyPy3 & merge sort & sys.stdin.readline() : 241676KB 1316ms
    - PyPy3 & sorted() & sys.stdin.readline() : 137240KB 672ms
    - Python3 & sorted() & sys.stdin.readline() : 84788KB 1336ms
Fail
    - * & * & input()

결론
    - PyPy3이 Python3보다 빠름
    - sys.stdin.readline()이 input()보다 빠름 (P/F 가름)
    - sorted()가 merge sort 보다 빠름

input() 이 sys.stdin.readline() 보다 느린 이유
    : input() 내장함수는 입력받은 값의 개행문자를 삭제시켜 리턴 (입력받은 문자열에 rstrip() 함수 적용)
      sys.stdin.readline()은 개행문자를 포함한 값을 리턴

sorted() vs sort() vs merge sort
    - sorted() : 정렬된 값을 반환하는 python의 내장함수
    - sort() : 배열 정렬 후 반환 X
    - sorted()와 sort()는 merge sort와 quick sort를 합해놓음 -> 최악의 경우에도 O(NlogN)
"""

import sys  # 제출할 때 import도 포함 (input() 대신 sys.stdin.readline() 사용했으므로)
sys.stdin = open("input.txt")

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]


ans = sorted(nums)
for i in range(N):
    print(ans[i])


# merge sort - 시간 초과 O(NlogN)
# def MergeSort(lst):
#     if len(lst) <= 1:
#         return lst
#
#     mid = len(lst) // 2
#     left = MergeSort(lst[:mid])
#     right = MergeSort(lst[mid:])
#     return merge(left, right)
#
# def merge(left, right):
#     sorted_lst = []
#     i = 0
#     j = 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             sorted_lst.append(left[i])
#             i += 1
#         else:
#             sorted_lst.append(right[j])
#             j += 1
#
#     while i < len(left):
#         sorted_lst.append(left[i])
#         i += 1
#
#     while j < len(right):
#         sorted_lst.append(right[j])
#         j += 1
#
#     return sorted_lst
# ans = MergeSort(nums)

# bubble sort - 시간 초과 O(N^2)
# for i in range(N):
#     for j in range(i, 0, -1):
#         if nums[j] < nums[j-1]:
#             nums[j], nums[j-1] = nums[j-1], nums[j]

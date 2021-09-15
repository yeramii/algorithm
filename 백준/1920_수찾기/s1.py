import sys
sys.stdin = open('input.txt')

N = int(input())
lst = list(map(int, input().split()))

M = int(input())
lst_M = list(map(int, input().split()))

## binary search : O(log n)
lst.sort()
for num in lst_M:
    l = 0
    r = N - 1
    is_find = False

    while l <= r:
        m = (l + r) // 2
        if num == lst[m]:
            print(1)
            is_find = True
            break
        elif num < lst[m]:
            r = m - 1
        else:
            l = m + 1

    if not is_find:
        print(0)

## in 사용 -> sequential search : O(n)
# for m in lst_M:
#     if m in lst_N:
#         idx = lst_N.index(m)
#         lst_N.pop(idx)
#         print(1)
#     else:
#         print(0)

'''
정렬만 되어 있으면 binary 가 빠르구나 ~

binary -> O(log n)
sequential -> O(n)

'''
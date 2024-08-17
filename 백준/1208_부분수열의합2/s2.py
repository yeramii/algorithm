"""
bisect : 이진 탐색을 쉽게 구현하게끔 해주는 함수
from bisect import bisect_left, bisect_right
    bisect_right(arr, n) : arr에서 n보다 큰 수가 있는 첫 번째 idx
    bisect_left(arr, n) : arr에서 n보다 크거나 같은 수가 있는 첫 번째 idx

"""
import sys
sys.stdin = open("input.txt")
from itertools import combinations
from bisect import bisect_left, bisect_right

def getNum(arr, find):
    return bisect_right(arr, find) - bisect_left(arr, find)

def getSum(arr, sumArr):
    for i in range(1, len(arr) + 1):
        for a in combinations(arr, i):
            sumArr.append(sum(a))
    sumArr.sort()

N, S = map(int, input().split())
nums = list(map(int, input().split()))

left, right = nums[:N//2], nums[N//2:]
leftSum, rightSum = [], []

getSum(left, leftSum)
getSum(right, rightSum)
ans = 0
for l in leftSum:
    find = S - l
    ans += getNum(rightSum, find)

ans += getNum(leftSum, S)
ans += getNum(rightSum, S)

print(ans)
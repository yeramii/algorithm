"""
Pass - 31120 44ms

내장함수로 대체 가능 - 33240KB 44ms
    - from itertools import combinations
    - from math import gcd
"""
import sys
sys.stdin = open("input.txt")

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def combination(arr, r):
    result = []
    def generate(chosen, start):
        if len(chosen) == r:
            result.append(chosen[:])    # 그냥 chosen을 넣으면 주소가 공유되어, chosen의 가장 마지막 상태([])가 일괄 적용됨 -> copy 필요
            return
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen, nxt+1)
            chosen.pop()
    generate([], 0)
    return result


for _ in range(int(input())):
    tc = list(map(int, input().split()))
    n, nums = tc[0], tc[1:]
    ans = 0
    for comb in combination(nums, 2):
        ans += gcd(comb[0], comb[1])
    #### 내장 함수로 대체 ####
    # from itertools import combinations
    # from math import gcd
    # for comb in combinations(nums, 2):
    #     ans += gcd(comb[0], comb[1])
    print(ans)

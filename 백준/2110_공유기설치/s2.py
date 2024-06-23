"""
Fail - 메모리 초과 (128MB 초과)
"""
import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10 ** 6)

N, C = map(int, input().split())
houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

def select_comb(arr, n):
    ans = []
    def generate(chosen, start):
        if len(chosen) == n:
            ans.append(chosen[:])
            return
        for i in range(start, len(arr)):
            chosen.append(arr[i])
            generate(chosen, i+1)
            chosen.pop(-1)
    generate([], 0)
    return ans

if C == 2:
    print(houses[1] - houses[0])
else:
    max_ans = 0
    for comb in select_comb(houses[1:-1], C-2):
        min_tmp = houses[-1] - comb[-1]
        tmp = [houses[0]]
        tmp.extend(comb)
        for i in range(len(comb)):
            if tmp[i+1] - tmp[i] < min_tmp:
                min_tmp = tmp[i+1] - tmp[i]
        if max_ans < min_tmp:
            max_ans = min_tmp
    print(max_ans)

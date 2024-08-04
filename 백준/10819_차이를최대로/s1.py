"""
Pass

1) 내장함수 - 31252KB 144ms
    from itertools import permutations
    permutations(lst, n)
2) 함수 만듬 - 36580KB 204ms

"""
import sys
sys.stdin = open("input.txt")
from itertools import permutations

### 1) 내장 함수
N = int(input())
lst = list(map(int, input().split()))
ans = 0
for p in permutations(lst, len(lst)):
    tmp = 0
    for i in range(N-1):
        tmp += abs(p[i] - p[i+1])
    ans = max(ans, tmp)
print(ans)

### 2) 함수 만듬
def perm(lst, n):
    visited = [0] * n
    result = []

    def generate(chosen, used):
        if len(chosen) == n:
            result.append(chosen[:])
            return
        for i in range(n):
            if not used[i]:
                used[i] = 1
                chosen.append(lst[i])
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], visited)
    return result

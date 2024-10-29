"""
Pass - 227036KB 5908ms
       229084KB 4688ms (elif 없앰)

knapsack
    - table을 그린 다음 코드로 변경하는게 이해하기 좋음
"""
import sys
sys.stdin = open("input.txt")

N, K = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

for r in range(1, N+1):
    for c in range(1, K+1):
        w, v = bag[r-1]
        if w > c:
            dp[r][c] = dp[r-1][c]
        elif w == c:    # elif 문은 없애도 됨 (어차피 c-w면 0이므로 else 문에서 0만 더해짐)
            dp[r][c] = max(dp[r-1][c], v)
        else:
            dp[r][c] = max(dp[r-1][c], v + dp[r-1][c-w])
print(dp[-1][-1])
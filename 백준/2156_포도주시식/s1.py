'''
Python3

처음에는 재귀로 할 방법밖에 떠오르지 않다가, 다른 사람의 DP 풀이를 참고했다.
-> DP는 경우의 수를 따져서, max 배열을 저장하는 것이 자주 나옴

풀이 : 각 포도주 자리에서 max로 마실 수 있는 양을 저장해 둠 = dp[]
    - i번째 자리에서 max로 마실 수 있는 경우는 아래 중 max 값으로 선택
        1) i번째를 마시지 않은 경우 = dp[i-1]
        2) i번째를 마시고 i-2번째까지 마신 경우 = grapes[i] + dp[i-2]
        3) i번째와 i-1번째를 마시고 i-3번째까지 마신 경우 = grapes[i] + grapes[i-1] + dp[i-3]

'''

import sys
sys.stdin = open('input.txt')

n = int(input())
grapes = [int(input()) for _ in range(n)]
dp = [grapes[0]]
if n >= 2:
    dp.append(grapes[0]+grapes[1])
if n >= 3:
    dp.append(max(dp[1], grapes[0]+grapes[2], grapes[1]+grapes[2]))
if n > 3:
    for i in range(3, n):
        dp.append(max(dp[i-1], grapes[i]+dp[i-2], grapes[i]+grapes[i-1]+dp[i-3]))
print(dp[-1])
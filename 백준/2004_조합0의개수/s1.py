"""
1. 팩토리얼 계산 - Fail (시간 초과)
2. 2와 5의 지수만 구함 - Pass (31252KB 44ms)
    - n!의 2의 지수 구하는 법 : n//2 + n//2^2 + n//2^3 + ...
    - n!의 5의 지수 구하는 법 : n//5 + n//5^2 + n//5^3 + ...
"""
import sys
sys.stdin = open("input.txt")
n, m = map(int, input().split())

# 1. 팩토리얼의 수를 계산한 후에, 0을 셈 -> Fail
# ans = 1
# for i in range(n, n-m, -1):
#     ans *= i / (i-n+m)
# tmp = str(int(ans))[::-1]
# zero = 0
# for i in str(int(ans))[::-1]:
#     if i == "0":
#         zero += 1
#     else:
#         break
# print(zero)


# 2. n!의 2와 5의 지수만 구함 -> Pass
def count(n, k):
    if n < k:
        return 0

    ans = 0
    while n >= k:
        ans += n // k
        n //= k
    return ans

print(min((count(n, 2)-count(m, 2)-count(n-m, 2)), (count(n, 5)-count(m, 5)-count(n-m, 5))))
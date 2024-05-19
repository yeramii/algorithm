"""
Pass - 55208KB 152ms
"""
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
data = {}
for _ in range(N):
    n = int(sys.stdin.readline())
    if n in data:
        data[n] += 1
    else:
        data[n] = 1

# sorted의 key 인자에서 lammbda 함수에 list 활용 -> 시간 초과 X
result = sorted(data.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])

# 가장 많은 수들의 key를 하나하나 비교함 -> 시간 초과
# ans = 2**62
# for item in data.items():
#     if item[1] == max(data.values()):
#         if item[0] < ans:
#             ans = item[0]
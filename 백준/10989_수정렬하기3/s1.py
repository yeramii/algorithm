"""
Pass
    - Python3 : 31120KB 8800ms
    - PyPy3 : 126200KB 2872ms
    => 시간 효율은 PyPy3, 메모리 효율은 Python3

메모리 제한이 있어 sort 함수 사용 대신 counting sort 진행
    - sort() : O(nlogn)
    - counting sort : O(n)
    - 만약, 입력으로 주어지는 수의 범위가 매우 크다면 dictionary 사용해야 할 것
"""
import sys
sys.stdin = open("input.txt")

# 메모리 초과 피하기 위해 counting sort 사용
N = int(sys.stdin.readline())
counts = [0] * 10001
for _ in range(N):
    counts[int(sys.stdin.readline())] += 1
for i, v in enumerate(counts):
    for _ in range(v):
        print(i)

# sorted : 메모리 초과
# nums = sorted(list(map(int, sys.stdin.readlines())))
# for num in nums:
#     print(num)
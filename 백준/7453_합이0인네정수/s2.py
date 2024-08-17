"""
Pass - PyPy3 1532944KB 9432ms

Counter
    - from collections import Counter
    - python의 기본 자료구조인 dictionary를 확장하고 있기 때문에, 사전에서 제공하는 API를 그대로 다 활용 가능

"""
import sys
sys.stdin = open("input.txt")
from collections import Counter

n = int(sys.stdin.readline())
A, B, C, D = [], [], [], []
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    A.append(tmp[0])
    B.append(tmp[1])
    C.append(tmp[2])
    D.append(tmp[3])

ab, cd = [i+j for i in A for j in B], [i+j for i in C for j in D]

cnt = 0
cd = Counter(cd)
for i in ab:
    cnt += cd[-i]   # cd에 없으면 0으로 출력
print(cnt)

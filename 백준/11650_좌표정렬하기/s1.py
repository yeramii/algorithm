"""
Pass - 46888KB 352ms

dictionary 사용법
    - "key" in dictionary : 해당 key가 dictionary에 존재하는지 확인
    - dictionary.keys() : dictionary의 key list를 반환
    - dictionary["key"] : key에 해당하는 value 반환
"""
import sys
sys.stdin = open("input.txt")

N = int(sys.stdin.readline())
data = {}
for _ in range(N):
    A, B = list(map(int, sys.stdin.readline().split()))
    if A in data:
        data[A].append(B)
    else:
        data[A] = [B]
for k in sorted(data.keys()):
    for v in sorted(data[k]):
        print(f"{k} {v}")
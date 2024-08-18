"""
Pass - defaultdict를 활용한 s2가 훨씬 효율적 (남의 풀이)

s1. Python3 (시간초과),         PyPy3 (211216KB 1964ms)
s2. Python3 (119028KB 740ms), PyPy3 (200800KB 528ms)
    defaultdict()
    from collections import defaultdict
    - dictionary를 만드는 dict 클래스의 서브 클래스
    - 인자로 주어진 객체(default-factory)의 기본값을 딕셔너리 값의 초기값으로 지정
        ex) int_dict = defaultdict(int) => 디폴트값이 int(0)인 딕셔너리
        ex) list_dict = defaultdict(list) => 디폴트값이 list([])인 딕셔너리
    - 키의 개수를 세야하는 상황이나, 리스트나 셋의 항목을 정리해야 하는 상황에 적절
        => 딕셔너리에 키가 있는지 확인 절차 거칠 필요 없이 바로 값을 1 증가시킬 수 있음
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
m, n = map(int, input().split())
A = [int(input()) for _ in range(m)]
B = [int(input()) for _ in range(n)]

inc, dec = [0], [0]
for l in range(1, m):
    for start in range(m):
        end = (start + l) % m
        if start < end:
            tmp = sum(A[start:end])
        else:
            tmp = sum(A[start:]) + sum(A[:end])
        if tmp <= N:
            inc.append(tmp)
if sum(A) <= N:
    inc.append(sum(A))
for l in range(1, n):
    for start in range(n):
        end = (start + l) % n
        if start < end:
            tmp = sum(B[start:end])
        else:
            tmp = sum(B[start:]) + sum(B[:end])
        if tmp <= N:
            dec.append(tmp)
if sum(B) <= N:
    dec.append(sum(B))
inc.sort()
dec.sort(reverse=True)

cnt = 0
i, d = 0, 0
while i < len(inc) and d < len(dec):
    if inc[i] + dec[d] < N:
        i += 1
    elif inc[i] + dec[d] > N:
        d += 1
    else:
        ii, dd = i, d
        while ii < len(inc) and inc[ii] == inc[i]:
            ii += 1
        while dd < len(dec) and dec[dd] == dec[d]:
            dd += 1
        cnt += (ii-i) * (dd-d)
        i, d = ii, dd
print(cnt)
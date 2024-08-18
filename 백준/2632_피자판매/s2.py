"""
Pass - Python3 (119028KB 740ms), PyPy3 (200800KB 528ms)

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
from collections import defaultdict

N = int(input())
m, n = map(int, input().split())
A = [int(input()) for _ in range(m)]
B = [int(input()) for _ in range(n)]

def find_case(pizza, length):
    case = defaultdict(int)
    for i in range(length):
        temp = pizza[i:] + pizza[:i]
        pre = 0
        for num in temp:
            pre += num
            case[pre] += 1
    case[sum(pizza)] = 1
    return case

case1 = find_case(A, m)
case2 = find_case(B, n)

result = case1.get(N, 0) + case2.get(N, 0)
for num in case1:
    if N -num in case2:
        result += case1[num] * case2[N-num]
print(result)
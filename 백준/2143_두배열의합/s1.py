"""
Pass

s1. 121644KB  424ms
    : 갯수를 저장해두기 위해 defaultdict 활용
s2.  71952KB 3540ms
    : 갯수를 구하기 위해 bisect 활용
"""
import sys
sys.stdin = open("input.txt")
from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

def find_case(lst, length):
    case = defaultdict(int)
    for i in range(length):
        tmp = lst[i:]
        s = 0
        for n in tmp:
            s += n
            case[s] += 1
    return case

caseA = find_case(A, n)
caseB = find_case(B, m)

ans = 0
for i in caseA:
    if T-i in caseB:
        ans += caseA[i] * caseB[T-i]
print(ans)
"""
Pass
1) hashmap
    - 151724KB 936ms
    - hash 자료구조의 구현 방식은 dictionary를 많이 사용
    - hashmap에서 해당 주소에 값이 없으면 값을 추가. 값이 있으면 그 값에 추가
2) Counter
    - 133316KB 640ms
    - from collections import Counter
        ex) Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
            => Counter({'hi': 3, 'hey': 2, 'hello': 1})
3) dict + binary search
    - 10816KB 4088ms
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
Ns = list(map(int, input().split()))
M = int(input())
Ms = list(map(int, input().split()))

### 1) hashing
d = dict()
for m in Ms:
    d[m] = 0
for n in Ns:
    if n in d.keys():
        d[n] = d[n] + 1
    else:
        d[n] = 0
ans = [str(d[m]) for m in Ms]
# print(' '.join(ans))


### 2) Counter
from collections import Counter
C = Counter(Ns)
# print(' '.join(str(C[m]) if m in C else '0' for m in Ms))


### 3) binary search
Ndict = dict()
Ns.sort()
for n in Ns:
    if n in Ndict:
        Ndict[n] += 1
    else:
        Ndict[n] = 1
ans = []
for m in Ms:
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        if m == Ns[mid]:
            end = mid
            break
        elif m > Ns[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if Ns[end] == m:
        ans.append(str(Ndict[m]))
    else:
        ans.append('0')
# print(' '.join(ans))
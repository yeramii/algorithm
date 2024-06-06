"""
Pass - 31120KB 36ms
"""
import sys
sys.stdin = open("input.txt")

N, K = map(int, input().split())
q = [i for i in range(1, N+1)]
idx = 0
ans = []
while N != 1:
    idx = (idx + K - 1) % N
    ans.append(q[idx])
    q.pop(idx)
    N -= 1
ans.append(q[0])
print("<" + repr(ans)[1:-1] + ">")

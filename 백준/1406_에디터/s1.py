"""
Fail - 시간 초과
    시간복잡도 : insert() >>> append(), pop()
        - append() : O(1)
        - pop() : O(1)
        - insert() : O(N)
"""
import sys
sys.stdin = open("input.txt")

S = [s for s in sys.stdin.readline().rstrip()]
cursor = len(S)
M = int(sys.stdin.readline())
for _ in range(M):
    tmp = sys.stdin.readline().split()
    if tmp[0] == "L":
        if cursor > 0:
            cursor -= 1
    elif tmp[0] == "D":
        if cursor < len(S):
            cursor += 1
    elif tmp[0] == "B":
        if cursor > 0:
            cursor -= 1
            S.pop(cursor)
    elif tmp[0] == "P":
        S.insert(cursor, tmp[1])
        cursor += 1
print(''.join(S))
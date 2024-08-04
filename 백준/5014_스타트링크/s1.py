"""
Pass - BFS : 72168KB 564ms

몫/나머지 구하는 등의 막구현으로 하려다가,
모든 조건의 반례를 다 생각하지 못해서 완전 탐색으로 틀었다.
"""
import sys
sys.stdin = open("input.txt")
from collections import deque

F, S, G, U, D = map(int, input().split())
def find_ans():
    visited = [0] * (F+1)
    visited[S] = 1
    q = deque([])
    q.append(S)
    while q:
        s = q.popleft()
        if s == G:
            return visited[s] - 1
        if s + U <= F and not visited[s + U]:
            visited[s + U] = visited[s] + 1
            q.append(s + U)
        if s - D >= 1 and not visited[s - D]:
            visited[s - D] = visited[s] + 1
            q.append(s - D)
    return -1


ans = find_ans()
print("use the stairs" if ans == -1 else ans)
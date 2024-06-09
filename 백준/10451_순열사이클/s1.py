"""
Pass - 31120KB 300ms
"""
import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    N = int(sys.stdin.readline())
    child = [0] + list(map(int, sys.stdin.readline().split()))
    cycle = 1
    visited = [0] * (N+1)
    for i in range(1, N+1):
        if visited[i]: continue
        while True:
            if not visited[i]:
                visited[i] = cycle
                i = child[i]
            else:
                cycle += 1
                break
    print(max(visited))
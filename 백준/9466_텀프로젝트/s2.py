"""
Fail - 시간 초과 at 78%

s1.py에 비해 부족한 점
- stack에서 같은 항목이 나올 때까지 pop 해서 visited를 1으로 만듬 & 남은 항목들도 pop해서 visited를 -1로 만듬
    => s1 에서는 같은 항목의 index를 찾아 자른 stack의 길이를 전체 cnt에서 빼줌. & visited는 T/F로만 기록
- visited에서 -1의 개수를 셈
    => s1 에서는 dfs를 진행하며 cnt를 계속 업데이트 해왔음
"""
import sys
sys.stdin = open("input.txt")

for _ in range(int(input())):
    n = int(input())
    child = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    for i in range(1, n+1):
        if visited[i]: continue
        stack = [i]
        v = i
        while True:
            w = child[v]
            if not visited[w]:
                if w in stack:
                    while stack[-1] != w:
                        visited[stack.pop()] = 1
                    visited[stack.pop()] = 1
                    break
                else:
                    stack.append(w)
                    v = w
            else:
                break
        for i in stack:
            visited[i] = -1
    print(visited.count(-1))
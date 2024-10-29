"""
Pass - 다른 사람의 풀이 참고

N-Queen 규칙
    - 상하좌우 및 대각선 방향으로는 다른 퀸이 있으면 안 됨 (거리 상관 X)

check로 상하 및 대각선 검사
    - visited에 저장된 값이 같으면 열이 같은 것
        -> visited[now_row] == visited[row]
    - 가로거리와 세로거리가 같으면 대각선인 것
        -> now_row - row == abs(visited[now_row] - visited[row])
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
visited = [-1] * N
cnt = 0


def check(now_row):
    for row in range(now_row):
        if visited[now_row] == visited[row] or now_row - row == abs(visited[now_row] - visited[row]):
            return False
    return True


def dfs(row):
    global cnt

    if row == N:
        cnt += 1
    else:
        for col in range(N):
            visited[row] = col
            if check(row):
                dfs(row + 1)

dfs(0)
print(cnt)


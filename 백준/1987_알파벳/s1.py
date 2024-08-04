"""
Pass - 164788KB 5980ms
     - 172232KB 6900ms (ord()를 dfs 내에서 호출할 때)

input data를 그대로 저장하는 것이 아닌, 미리 ord()로 변환한 후 저장
-> arr의 각 칸을 검사할 때마다 ord() 변환하지 않아도 되므로 시간 효율 증가
"""
def dfs(r, c, cnt):
    global ans, alphabets, visited
    if not alphabets[arr[r][c]]:
        alphabets[arr[r][c]] = 1
        ans = max(ans, cnt+1)
        for k in range(4):
            rr = r + dr[k]
            cc = c + dc[k]
            if rr in range(R) and cc in range(C) and not visited[rr][cc]:
                visited[rr][cc] = 1
                dfs(rr, cc, cnt+1)
                visited[rr][cc] = 0
        alphabets[arr[r][c]] = 0
    return

R, C = map(int, input().split())
arr = [list(map(lambda x: ord(x)-65, input())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
visited[0][0] = 1
alphabets = [0] * 26
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
ans = 0
dfs(0, 0, 0)
print(ans)
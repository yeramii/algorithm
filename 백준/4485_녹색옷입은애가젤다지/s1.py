import heapq

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

tc = 1
while True:
    N = int(input())
    if N == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    ans = [[1250] * N for _ in range(N)]
    ans[0][0] = cave[0][0]
    q = [(ans[0][0], 0, 0)]     # cost, R, C
    while q:
        cost, r, c = heapq.heappop(q)
        for k in range(4):
            rr = r + dr[k]
            cc = c + dc[k]
            if rr not in range(N) or cc not in range(N):
                continue
            new_cost = cost + cave[rr][cc]
            if new_cost < ans[rr][cc]:
                ans[rr][cc] = new_cost
                heapq.heappush(q, (new_cost, rr, cc))

    print(f"Problem {tc}: {ans[N-1][N-1]}")
    tc += 1
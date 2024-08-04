"""
Pass - 31120KB 936ms

경우의 수
    1) R이 1인 경우 -> 1~C 중 2개 골라서 자른 group들을 모두 비교 => ㅣㅣ 로 자름
    2) C가 1인 경우 -> 1~R 중 2개 골라서 자른 group들을 모두 비교 => = 로 자름
    3) 1)2)가 아닌 경우 -> (r, c) 기준 4등분한 group에서 차례대로 2개씩 묶어 비교
        -> 4분면으로 나누는 것이 아니라 1) 2) 처럼 ㅣㅣ = 로 나누는 경우도 고려해야 함

sum()
    - 2차원 배열 더하는 경우, 아래 에러 발생
        ex) lst = [[1], [2, 3]]
            sum(lst)
        =>  TypeError: unsupported operand type(s) for +: 'int' and 'list'

    - 빈 리스트를 같이 입력해주면 해결!
        ex) sum(lst, [])
        =>  [1, 2, 3]
    - 한 번 더 sum하면 상수 출력
        ex) sum(sum(lst, []))
        =>  6
"""
import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
arr = []
for n in range(N):
    tmp = []
    for s in input().strip():
        tmp.append(int(s))
    arr.append(tmp)

def split_4group(R, C):
    tmp1, tmp2, tmp3, tmp4 = 0, 0, 0, 0
    for r in range(R):
        for c in range(C):
            tmp1 += arr[r][c]
        for c in range(C, M):
            tmp2 += arr[r][c]
    for r in range(R, N):
        for c in range(C):
            tmp3 += arr[r][c]
        for c in range(C, M):
            tmp4 += arr[r][c]
    return [tmp1, tmp2, tmp4, tmp3]

def choose_2(n):
    tmp = []
    for i in range(1, n):
        for j in range(i+1, n):
            tmp.append((i, j))
    return tmp

ans = 0
if N == 1 or M == 1:
    if N == 1:
        group = choose_2(M)
        for g in group:
            tmp = sum(arr[0][:g[0]]) * sum(arr[0][g[0]:g[1]]) * sum(arr[0][g[1]:])
            ans = max(tmp, ans)
    elif M == 1:
        group = choose_2(N)
        for g in group:
            tmp1, tmp2, tmp3 = 0, 0, 0
            for c in range(g[0]):
                tmp1 += arr[c][0]
            for c in range(g[0], g[1]):
                tmp2 += arr[c][0]
            for c in range(g[1], N):
                tmp3 += arr[c][0]
            ans = max(ans, tmp1*tmp2*tmp3)
else:
    for r in range(1, N):
        for c in range(1, M):
            tmp = split_4group(r, c)
            ans = max(ans,
                      (tmp[0]+tmp[1])*tmp[2]*tmp[3],
                      tmp[0]*(tmp[1]+tmp[2])*tmp[3],
                      tmp[0] * tmp[1] * (tmp[2] + tmp[3]),
                      (tmp[0]+tmp[3])*tmp[1]*tmp[2])
    group = choose_2(M)
    for g in group:
        tmp1, tmp2, tmp3 = 0, 0, 0
        for r in range(N):
            for c in range(g[0]):
                tmp1 += arr[r][c]
            for c in range(g[0], g[1]):
                tmp2 += arr[r][c]
            for c in range(g[1], M):
                tmp3 += arr[r][c]
        ans = max(tmp1 * tmp2 * tmp3, ans)
    group = choose_2(N)
    for g in group:
        tmp1 = sum(sum(arr[:g[0]], []))
        tmp2 = sum(sum(arr[g[0]:g[1]], []))
        tmp3 = sum(sum(arr[g[1]:], []))
        ans = max(tmp1 * tmp2 * tmp3, ans)
print(ans)

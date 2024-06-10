"""
Pass - 31228KB 44ms

sort 할 때는 int와 str을 항시 조심할 것 ..
str로 저장해도 int로 sort하고 싶을 땐 sort(lambda x: int(x)) 와 같이 lambda 함수 사용할 것
"""
import sys
sys.stdin = open("input.txt")

def find_dangi(r, c, curr):
    global arr, cnt

    if arr[r][c] == "1":
        arr[r][c] = curr
        cnt += 1
    else:
        return
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if rr in range(N) and cc in range(N):
            find_dangi(r+dr[i], c+dc[i], curr)


N = int(input())
arr = []
for _ in range(N):
    tmp = []
    for i in input():
        tmp.append(i)
    arr.append(tmp)
house = []
curr = 1
for r in range(N):
    for c in range(N):
        if arr[r][c] != "1": continue
        curr += 1
        cnt = 0
        find_dangi(r, c, curr)
        house.append(str(cnt))
house.sort(key=lambda x: int(x))
print(curr-1)
print('\n'.join(house))

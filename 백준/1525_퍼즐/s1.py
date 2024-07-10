"""
Pass - 56152KB 576ms

1. 탐색 - dictionary vs. list
    - dictionary : O(1)
        . key-value 쌍을 저장하는 구조
        . in 연산자로 key를 찾을 때, hash 함수를 이용하여 해당 key가 존재하는지 확인
    - list : O(n)
        . 순서가 있는 항목들의 모임 (각 항목에 index 부여)
        . in 연산자로 항목을 찾을 때, 처음부터 끝까지 순차적으로 비교하는 선형탐색 수행
2. 반례
    - 원소가 3열일 때 +1인 경우, 1열일 때 -1인 경우를 놓침
"""
import sys
sys.stdin = open("input.txt")
from collections import deque

arr = ""
for _ in range(3):
    arr += ''.join(input().split())
ans = "123456780"
# visited = [arr]
visited = { arr: 0 }
q = deque([])
q.append((arr, 0))

def bfs():
    while q:
        a, c = q.popleft()
        if a == ans:
            return c
        idx = a.index('0')
        for k in [-3, -1, 1, 3]:
            if idx + k in range(9):
                if k in [-1, 1] and (idx+k)//3 != idx//3: continue
                tmp = list(a)
                tmp[idx], tmp[idx+k] = tmp[idx+k], tmp[idx]
                j_tmp = ''.join(tmp)
                if j_tmp not in visited:
                    q.append((j_tmp, c+1))
                    # visited.append(j_tmp)
                    visited[j_tmp] = c+1
    return -1
print(bfs())
"""
Pass - 44580KB 4140ms

다른 사람의 코드로 배운 점

    - sort() : 2차원 배열도 오름 차순 가능함
    - print(*objects, sep=' ', end='\n', file=None, flush=False) : 우선 나열하면 한 칸 씩 띄어서 출력됨
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
data = []
for _ in range(N):
    A, B = map(int, input().split())
    data.append((A, B))
data.sort()
for i in range(N):
    print(data[i][0], data[i][1])
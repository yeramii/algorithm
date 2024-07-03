"""
Pass - 59068KB 4232ms

조건 누락해서 몇 번 Fail 함
  1) start와 end와 next start가 모두 같을 수 있음을 간과 - 조건 누락!
  2) 끝나는 시간만 정렬하고  시작하는 시간은 정렬 안 함 - TC에 속음!
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))
next_start = 0
cnt = 0
for meeting in meetings:
    if meeting[0] >= next_start:
        cnt += 1
        next_start = meeting[1]
print(cnt)
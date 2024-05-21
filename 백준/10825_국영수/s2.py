"""
Pass - 87500KB 396ms

iterables.sort(key=lambda x: (-int(x[1]),int(x[2]), -int(x[3]), x[0]))
    - 리스트 내의 우선 순위에 맞게 원소 정렬
      ex) 원소 순서 : 1 내림 -> 2 오름 -> 3 내림 -> 0 오름
    - 이처럼 lambda 함수를 이용하면 특정 기준으로 정렬하는 대부분의 문제를 해결할 수 있다.
"""
import sys
sys.stdin = open('input.txt')

N = int(input())
scores = []
for _ in range(N):
    scores.append(sys.stdin.readline().split())
for score in sorted(scores, key=lambda x: (-int(x[1]),int(x[2]), -int(x[3]), x[0])):
    print(score[0])
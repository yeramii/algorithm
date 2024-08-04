"""
Pass
누적합에 비해 투 포인터가 훨씬 시간 효율적 (메모리도 감소)

1) 누적합 - PyPy3 110704KB 232ms (Python3 시간 초과)
2) 투 포인터 - PyPy3 109240KB 96ms (Python3 32140KB 36ms)
    - two pointers' algorithm
        1. 시작점(start)과 끝점(end)이 첫 번째 원소의 index(0)를 가리키도록 한다.
        2. 현재 부분 합이 M과 같다면, 카운트한다.
        3. 현재 부분 합이 M보다 작거나 같다면, end를 1 증가시킨다.
        4. 현재 부분 합이 M보다 크다면, start를 1 증가시킨다.
        5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다.
    => 리스트 내 원소에 음수가 포함되어 있다면 적용 불가! (양수 only)
"""
import sys
sys.stdin = open("input.txt")
N, M = map(int, input().split())
A = list(map(int, input().split()))
acc = [0]
tmp = 0
for i in range(0, N):
    tmp += A[i]
    acc.append(tmp)

# 1) 누적합
# cnt = 0
# for i in range(N+1):
#     for j in range(i):
#         if acc[i] - acc[j] == M:
#             cnt += 1
# print(cnt)

# 2) 투 포인터 (two pointers)
def twopointers():
    s, e = 0, 0
    subsum = A[0]
    cnt = 0
    while True:
        if subsum < M:
            e += 1
            if e >= N:
                break
            subsum += A[e]
        elif subsum == M:
            cnt += 1
            subsum -= A[s]
            s += 1
        else:
            subsum -= A[s]
            s += 1
    return cnt
print(twopointers())
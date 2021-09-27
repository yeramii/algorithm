import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    points = list(map(int, input().split()))
    checks = [0 for _ in range(N)]
    checks[M] = 1

    cnt = 0
    while True:
        if points[0] == max(points):
            cnt += 1

            if checks[0]:
                print(cnt)
                break
            else:
                points.pop(0)
                checks.pop(0)

        else:
            points.append(points.pop(0))
            checks.append(checks.pop(0))

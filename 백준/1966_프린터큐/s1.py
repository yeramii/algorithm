import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    points = list(map(int, input().split()))

    cnt = 0
    front = 0
    rear = N - 1
    while True:
        m_value = max(points)
        if max(points[front:]) == m_value:
            m_idx = points[front:].index(m_value) + front
        else:
            m_idx = points.index(m_value)
        cnt += 1

        points.pop(m_idx)
        N -= 1
        if m_idx == M:
            break
        elif m_idx > M:
            if m_idx == N:
                front = 0
            else:
                front = m_idx
        else:
            front = m_idx
            M -= 1
        rear = (N + front - 1) % N

    print(cnt)

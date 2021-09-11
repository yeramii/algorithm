"""
Runtime Error
푸는 중 ㅠㅠ
"""

import sys
sys.stdin = open('input.txt')

N = int(input())
students = [[0] for _ in range(N ** 2 + 1)]
classroom = [[0] * (N + 2) for _ in range(N + 2)]

# 첫 번째 학생
student, *lst = map(int, input().split())
students[student] = lst
classroom[2][2] = student

# 나머지 학생
for _ in range(N ** 2 - 1):
    # 학생들의 리스트에 저장
    student, *lst = map(int, input().split())
    students[student] = lst

    # 첫 번째 조건 검사
    max_score = 0
    length = 0
    temp_max = []
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if not classroom[r][c]:
                temp = 0
                if classroom[r - 1][c] in lst:
                    temp += 1
                if classroom[r + 1][c] in lst:
                    temp += 1
                if classroom[r][c + 1] in lst:
                    temp += 1
                if classroom[r][c - 1] in lst:
                    temp += 1
                if temp and temp == max_score:
                    temp_max.append([r, c])
                    length += 1
                elif temp > max_score:
                    temp_max = [[r, c]]
                    max_score = temp
                    length = 1

    # 두 번째 조건 검사
    if not length:
        adj_score = 0
        temp_adj = 0
        empty = []
        for r in range(1, N + 1):
            for c in range(1, N + 1):
                if not classroom[r][c]:
                    empty.append([r, c])
                    temp = 0
                    if not classroom[r - 1][c] and (r - 1) != 0:
                        temp += 1
                    if not classroom[r + 1][c] and (r + 1) != (N + 1):
                        temp += 1
                    if not classroom[r][c + 1] and (c + 1) != (N + 1):
                        temp += 1
                    if not classroom[r][c - 1] and (c - 1) != 0:
                        temp += 1
                    if temp == 4:
                        classroom[r][c] = student
                    elif temp and temp == adj_score:
                        temp_adj.append([r, c])
                        length += 1
                    elif temp > adj_score:
                        temp_adj = [[r, c]]
                        adj_score = temp
                        length = 1
        if not length:
            classroom[empty[0][0]][empty[0][1]] = student
        else:
            classroom[temp_adj[0][0]][temp_adj[0][1]] = student

    elif length == 1:
        classroom[temp_max[0][0]][temp_max[0][1]] = student

    else:
        adj_score = 0
        length = 0
        temp_adj = []

        for seat in temp_max:
            r = seat[0]
            c = seat[1]
            temp = 0
            if not classroom[r - 1][c] and (r - 1) != 0:
                temp += 1
            if not classroom[r + 1][c] and (r + 1) != (N + 1):
                temp += 1
            if not classroom[r][c + 1] and (c + 1) != (N + 1):
                temp += 1
            if not classroom[r][c - 1] and (c - 1) != 0:
                temp += 1
            if temp == 4:
                classroom[r][c] = student
            elif temp and temp == adj_score:
                temp_adj.append([r, c])
                length += 1
            elif temp > adj_score:
                temp_adj = [[r, c]]
                adj_score = temp
                length = 1

        if not length:
            classroom[temp_max[0][0]][temp_max[0][1]] = student
        else:
            classroom[temp_adj[0][0]][temp_adj[0][1]] = student

# 만족도 검사
scores = [0, 0, 0, 0, 0]
for r in range(1, N + 1):
    for c in range(1, N + 1):
        temp = 0
        if (r - 1) != 0 and classroom[r - 1][c] in students[classroom[r][c]]:
            temp += 1
        if (r + 1) != (N + 1) and classroom[r + 1][c] in students[classroom[r][c]]:
            temp += 1
        if (c + 1) != (N + 1) and classroom[r][c + 1] in students[classroom[r][c]]:
            temp += 1
        if (c - 1) != 0 and classroom[r][c - 1] in students[classroom[r][c]]:
            temp += 1
        scores[temp] += 1

total = scores[1] + scores[2]*10 + scores[3]*100 + scores[4]*1000
print(total)
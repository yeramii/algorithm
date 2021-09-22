import sys
sys.stdin = open('input2.txt')

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
score = [0, 1, 10, 100, 1000]


def find_cnt(r, c, student):
    like_cnt = 0
    void_cnt = 0

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if not classroom[nr][nc]:
                void_cnt += 1
            elif classroom[nr][nc] in like[student]:
                like_cnt += 1

    return like_cnt, void_cnt


def find_pos(student):
    result = []
    for r in range(N):
        for c in range(N):
            if classroom[r][c]:
                continue
            like_cnt, void_cnt = find_cnt(r, c, student)
            result.append((like_cnt, void_cnt, r, c))

    result.sort(key=lambda x: (x[0], x[1], -x[2], -x[3]), reverse=True)
    row, col = result[0][2], result[0][3]
    return row, col


N = int(input())
classroom = [[0] * N for _ in range(N)]
like = dict()

# 자리 배치
for _ in range(N * N):
    student, *lst = map(int, input().split())
    like[student] = lst
    r, c = find_pos(student)
    classroom[r][c] = student


# 만족도 계산
total = 0
for r in range(N):
    for c in range(N):
        total += score[find_cnt(r, c, classroom[r][c])[0]]
print(total)

'''
dict 활용
key=lambda x 활용
'''
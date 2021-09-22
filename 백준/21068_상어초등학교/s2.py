import sys
sys.stdin = open('input2.txt')

N = int(input())
students = [[0] for _ in range(N ** 2 + 1)]
classroom = [[0] * (N + 2) for _ in range(N + 2)]

# 첫 번째 학생
student, *lst = map(int, input().split())
students[student] = lst
classroom[2][2] = student


def decide_chair():
    candidate = []
    idx = -1
    max_prefer = 0
    max_empty = 0
    max_idx = 0

    student, *lst = map(int, input().split())
    students[student] = lst

    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if not classroom[r][c]:
                idx += 1
                
                # candidate index, row, col, num of prefer, num of empty
                temp_candidate = [idx, r, c, 0, 0]
                is_prefer, is_empty = examine_condition(r + 1, c, lst)
                temp_candidate[3] += is_prefer
                temp_candidate[4] += is_empty
                is_prefer, is_empty = examine_condition(r - 1, c, lst)
                temp_candidate[3] += is_prefer
                temp_candidate[4] += is_empty
                is_prefer, is_empty = examine_condition(r, c + 1, lst)
                temp_candidate[3] += is_prefer
                temp_candidate[4] += is_empty
                is_prefer, is_empty = examine_condition(r, c - 1, lst)
                temp_candidate[3] += is_prefer
                temp_candidate[4] += is_empty

                if temp_candidate[3] > max_prefer:
                    max_prefer = temp_candidate[3]
                    max_empty = temp_candidate[4]
                    max_idx = idx
                elif temp_candidate[3] == max_prefer:
                    if temp_candidate[4] > max_empty:
                        max_empty = temp_candidate[4]
                        max_idx = idx

                candidate.append(temp_candidate)

    classroom[candidate[max_idx][1]][candidate[max_idx][2]] = student


def examine_condition(r, c, lst):
    """
    해당 행과 열이 범위안에 있을 때,
    선호하는 학생이면 is_prefer를 True로, 비어있으면 is_empty를 True로 반환

    """
    is_prefer = False
    is_empty = False

    if r in range(1, N + 1) and c in range(1, N + 1):
        temp = classroom[r][c]
        if not temp:
            is_empty = True
        elif temp in lst:
            is_prefer = True

    return is_prefer, is_empty


# 나머지 학생들 자리 정하기
for _ in range(N ** 2 - 1):
    decide_chair()


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
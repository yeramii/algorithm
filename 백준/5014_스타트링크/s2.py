F, S, G, U, D = map(int, input().split())
def find_ans():
    if S == G:
        return 0
    if S + U > F and S - D < 1:
        return -1
    if S < G:
        if not U:
            return -1
        if ((G - S) % U) % D:
            return -1
        tmp = (G - S) // U
        cnt_U = tmp + 1 if (G - S) % U else tmp
        cnt_D = (G - S - U * cnt_U) // D
    elif S > G:
        if not D:
            return -1
        if ((S - G) % D) % U:
            return -1
        tmp = (S - G) // D
        cnt_D = tmp + 1 if (S - G) % D else tmp
        cnt_U = (S - G - D * cnt_D) // U
    return abs(cnt_D) + abs(cnt_U)

ans = find_ans()
print("use the stairs" if ans == -1 else ans)
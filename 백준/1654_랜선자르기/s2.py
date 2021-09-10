import sys
sys.stdin = open('input.txt')


K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

memo1 = [0, min(lans)]  # [0, 457, 401, 267, 200, ...]
memo2 = [0]             # [0, 4, 5, 9, 11, ...]

def calc_memo1(idx):
    result = 0
    for lan in lans:
        temp = lan // idx
        if temp > result:
            result = temp
    return result

def calc_memo2(m1):
    result = 0
    for lan in lans:
        result += lan // m1
    return result

def find_maxlen():
    idx = 1

    while True:
        if memo2[idx] == N:
            return memo1[idx]
        elif memo2[idx] < N:
            idx += 1
            memo1.append(calc_memo1(idx))
            memo2.append(calc_memo2(memo1[idx]))
        else:
            u_bound = memo1[idx - 1] - 1
            while True:
                if calc_memo2(u_bound) >= N:
                    return u_bound
                else:
                    u_bound -= 1

memo2.append(calc_memo2(memo1[1]))
print(find_maxlen())

print(memo1)
print(memo2)
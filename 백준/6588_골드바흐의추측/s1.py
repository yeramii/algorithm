"""
Pass - 50604KB 2656ms

반례 찾느라 오래 걸림
"""
import sys
sys.stdin = open("input.txt")

tc = []
while True:
    tmp = int(sys.stdin.readline().strip())
    if not tmp: break
    tc.append(tmp)

prime = [False, False] + [True] * (max(tc)-1)
for n in range(2, int(max(tc) ** 0.5) + 1):
    if prime[n]:
        for i in range(n * 2, max(tc) + 1, n):
            prime[i] = False

for t in tc:
    for i in range(3, t//2 + 1, 2):     # 6=3+3의 경우, end가 t//2면 range(3, 3, 2)이므로 for문 미가동
        if prime[i] and prime[t-i]:
            print(f"{t} = {i} + {t-i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
import sys
sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
max_num = nums[-1]
prime = [False, False] + [True] * (max_num - 1)
cnt = 0

for num in range(2, int(max_num**(1/2)) + 1):
    if prime[num]:
        for i in range(2 * num, max_num + 1, num):
            prime[i] = False

for num in nums:
    if prime[num]:
        cnt += 1

print(cnt)

'''
[에라토스테네스의 체]
소수 판정하려면 해당 수의 제곱근까지 약수가 있는지 판단하면 된다.
'''
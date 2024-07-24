# 1. 내장 함수
from itertools import permutations
from itertools import combinations

data = permutations([1,2,3,4], 2)
print(list(data))

data = combinations([1,2,3,4], 2)
print(list(data))

# 2. 재귀 구현
def permutation(arr, r):
    # DFS 와 checklist 사용
    used = [0 for _ in range(len(arr))]
    result = []

    def generate(chosen, used):
        if len(chosen) == r:
            result.append(chosen[:])
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)
    return result
# print(permutation("ABCD", 2))
# print(permutation([1,2,3,4,5], 3))


def combination(arr, r):
    result = []
    def generate(chosen, start):
        import copy
        if len(chosen) == r:
            # WARNING: chosen 리스트가 재귀 호출에서 공유되고 있기 때문에, chosen 리스트의 참조가 추가되지 않고,
            # chosen 리스트의 참조가 공유되어 모든 조합이 마지막에 추가된 chosen의 상태를 가리킴
            # => chosen의 복사본을 추가해야 함
            result.append(copy.deepcopy(chosen))
            return

        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen, nxt + 1)
            chosen.pop()
    generate([], 0)
    return result
# print(combination("ABCD", 2))
# print(combination([1,2,3,4,5], 3))

'''
Python3 - Pass (3476ms)

다른 사람들 풀이 => Binary Search
    1;

[느낀점]
    이진 탐색이라고, 굳이 자료가 정렬되어 있을 필요 없다.
    비교 대상만 반 나눠 따져도 연산량이 많이 줄게 된다 !

'''

import sys
sys.stdin = open('input2.txt')

N, M = map(int, input().split())
trees = list(map(int, input().split()))

end = max(trees)
start = 1

def cutTree(h):
    '''
    h 높이로 잘랐을 때, 얻어지는 총 나무의 길이 반환
    '''
    res = 0
    for t in trees:
        if t - h > 0:
            res += (t - h)
    return res

while start <= end:
    mid = (start + end) // 2
    res = cutTree(mid)

    if res < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)
# start 와 end 가 교차돼야 while 문이 끝나기 때문에
# mid 는 (start+end)//2고, 이는 더 작은 수인 end 이다. => 답: end

'''
아래 코드도 답은 같지만, 연산량이 많아서 시간 초과였다.

    if res < M:
        end = mid
    elif res > M:
        start = mid
    else:
        break

print(mid)
'''
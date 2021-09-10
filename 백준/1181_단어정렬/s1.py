import sys
sys.stdin = open('input.txt')

N = int(input())
temp = [input() for _ in range(N)]

# 단어 사전 순 정렬 & 중복 제거
words = list(set(temp))
words.sort()

result = sorted(words, key=lambda x: len(x))
for word in result:
    print(word)


# # 짧은 순서대로 출력
# length = 1
# while words:
#     for idx, word in enumerate(words):
#         if len(word) == length:
#             print(word)
#             words.pop(idx)
#             break
#
#         if word == words[-1]:
#             length += 1


# # 단어 길이 저장할 리스트
# lst = []
# for word in words:
#     lst.append(len(word))
# lst.sort()
#
# # 짧은 순서대로 출력
# for length in lst:
#     for idx, word in enumerate(words):
#         if len(word) == length:
#             print(word)
#             words.pop(idx)
#             break
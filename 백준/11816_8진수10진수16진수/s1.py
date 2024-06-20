"""
Pass
1) int(string, base=10) - 31120KB 68ms
2) **                   - 31120KB 44ms
"""
import sys
sys.stdin = open("input.txt")

X = input().strip()

### 1) int(string, base=10)
if X[0] == '0' and len(X) != 1:
    if len(X) >= 2 and X[1] == 'x':
        # 16진수
        print(int(X, 16))
    else:
        # 8진수
        print(int(X, 8))
else:
    # 10진수
    print(X)

### 2) **
for16 = "0123456789abcdef"
if X[0] == '0' and len(X) != 1:
    if len(X) >= 2 and X[1] == 'x':
        # 16진수
        ans = 0
        for i, c in enumerate(X[-1:1:-1]):
            ans += for16.index(c) * (16 ** i)
        print(ans)
    else:
        # 8진수
        ans = 0
        for i, c in enumerate(X[-1:0:-1]):
            ans += for16.index(c) * (8 ** i)
        print(ans)
else:
    # 10진수
    print(X)

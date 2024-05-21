import sys
sys.stdin = open("input.txt")

for _ in range(int(input())):
    stack = []
    top = -1
    tmp = input()
    for i in tmp:
        if i == "(":
            top += 1
            stack.append(i)
        elif i == ")":
            if top > -1 and stack[top] == "(":
                stack.pop(top)
                top -= 1
            else:
                print("NO")
                break
    # for 문을 break 등으로 빠져 나오지 않고 완전히 돈 경우에 실행
    else:
        if not stack and top == -1:
            print("YES")
        else:
            print("NO")

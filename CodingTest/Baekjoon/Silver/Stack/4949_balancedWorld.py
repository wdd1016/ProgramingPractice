import sys

input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == ".":
        break
    stack = []
    for char in string:
        if char == "[":
            stack.append(char)
        elif char == "(":
            stack.append(char)
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
        elif char == ".":
            if stack:
                print("no")
            else:
                print("yes")

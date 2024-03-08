import sys

input = sys.stdin.readline

m = int(input())

s = set()

for _ in range(m):
    string = input().rstrip()
    if string == "all":
        s = set([i for i in range(1, 21)])
        continue
    elif string == "empty":
        s.clear()
        continue

    command, number = string.split()
    number = int(number)
    if command == "add":
        s.add(number)
    elif command == "remove":
        s.discard(number)
    elif command == "check":
        print(int(number in s))
    elif command == "toggle":
        if number in s:
            s.discard(number)
        else:
            s.add(number)

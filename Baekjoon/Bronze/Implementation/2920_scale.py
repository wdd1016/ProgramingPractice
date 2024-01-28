import sys

input = sys.stdin.readline

lst = list(map(int, input().split()))

if lst[0] == 1:
    for i in range(7):
        if lst[i] > lst[i + 1]:
            print("mixed")
            break
        if i == 6:
            print("ascending")
elif lst[0] == 8:
    for i in range(7):
        if lst[i] < lst[i + 1]:
            print("mixed")
            break
        if i == 6:
            print("descending")
else:
    print("mixed")

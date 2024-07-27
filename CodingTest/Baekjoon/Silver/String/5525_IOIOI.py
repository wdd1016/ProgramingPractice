import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
string = input().rstrip()

needle = "IO" * n + "I"
count = 0

try:
    i = string.index(needle) + len(needle)
    count += 1
    while i < len(string) - 2:
        if string[i : i + 2] == "OI":
            i += 2
            count += 1
        else:
            i = string.index(needle, i) + len(needle)
            count += 1
    print(count)
except:
    print(count)

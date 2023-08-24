import sys
input = sys.stdin.readline

str1 = input().strip()
for i in range(len(str1) // 2):
    if (len(str1) == 1):
        print(1)
        break
    if (str1[i] != str1[-(i+1)]):
        print(0)
        break
    if (i == (len(str1) // 2) - 1):
        print(1)
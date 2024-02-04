import sys

input = sys.stdin.readline

l = int(input())
str1 = input().rstrip()
magicNumber = ord("a") - 1

answer = 0
for i in range(l - 1, -1, -1):
    answer = (answer * 31) % 1234567891
    answer += ord(str1[i]) - magicNumber

print(answer)

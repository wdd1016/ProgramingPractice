import sys

input = sys.stdin.readline

n = int(input())

answer = 1
for i in range(1, n + 1):
    answer = answer * i

count = 0
while True:
    if answer % 10 != 0:
        break
    answer = answer // 10
    count += 1

print(count)

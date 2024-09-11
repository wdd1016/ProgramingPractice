import sys

input = sys.stdin.readline

progression = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(10, 100):
    progression.append(progression[i - 1] + progression[i - 5])

t = int(input())

for _ in range(t):
    print(progression[int(input()) - 1])

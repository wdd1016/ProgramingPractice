import sys

input = sys.stdin.readline

n, k = map(int, input().split())
table = list(input().rstrip())

count = 0
for i in range(len(table)):
    if table[i] == "P":
        for j in range(i - k, i + k + 1):
            if j < 0:
                j = -1
            elif j >= n:
                break
            elif table[j] == "H":
                count += 1
                table[j] = "X"
                break

print(count)

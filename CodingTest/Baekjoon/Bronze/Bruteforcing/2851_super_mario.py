import sys

input = sys.stdin.readline

sum = 0

for _ in range(10):
    n = int(input())
    if sum + n < 100:
        sum += n
    elif sum + n == 100:
        sum += n
        break
    else:
        if sum + n - 100 <= 100 - sum:
            sum += n
            break
        else:
            break

print(sum)

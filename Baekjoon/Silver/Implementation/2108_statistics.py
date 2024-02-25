import sys
import statistics

input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]

lst.sort()

print(round(sum(lst) / n))
print(lst[n // 2])

temp = statistics.multimode(lst)
if len(temp) > 1:
    print(temp[1])
else:
    print(temp[0])

print(lst[-1] - lst[0])

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
for i in range(1, n + 1):
    if (n % i == 0):
        lst.append(i)
if (len(lst) < k):
    print(0)
else:
    print(lst[k - 1])
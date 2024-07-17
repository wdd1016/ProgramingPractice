import sys

input = sys.stdin.readline


def countLAN(lst, length):
    count = 0
    for i in lst:
        count += i // length
    return count


k, n = map(int, input().split())
lst = []

for _ in range(k):
    lst.append(int(input()))

minLength = min(lst) // ((n // k) + 1)
maxLength = max(lst) // (n // k)

while minLength <= maxLength:
    length = (minLength + maxLength) // 2
    if length == 0:
        length = 1
    count = countLAN(lst, length)
    if count < n:
        maxLength = length - 1
    else:
        minLength = length + 1

print(minLength - 1)

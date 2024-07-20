import sys

input = sys.stdin.readline

n = int(input())
times = int(input())
recos = list(map(int, input().split()))


def popStudent(photozone, count):
    idx = count.index(min(count))
    photozone.pop(idx)
    count.pop(idx)


photozone = []
count = []
for reco in recos:
    if reco not in photozone:
        if len(photozone) == n:
            popStudent(photozone, count)
        photozone.append(reco)
        count.append(1)
    else:
        count[photozone.index(reco)] += 1

photozone.sort()
print(*photozone)

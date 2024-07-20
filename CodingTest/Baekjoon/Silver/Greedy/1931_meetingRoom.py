import sys

input = sys.stdin.readline

n = int(input())

meeting = []

for _ in range(n):
    startTime, endTime = map(int, input().split())
    meeting.append([startTime, endTime])

meeting.sort(key=lambda x: (x[1], x[0]))

endTime = meeting[0][1]
count = 1

for i in range(1, n):
    if meeting[i][0] >= endTime:
        count += 1
        endTime = meeting[i][1]

print(count)

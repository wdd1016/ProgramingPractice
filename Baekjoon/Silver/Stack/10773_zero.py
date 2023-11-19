import sys
input = sys.stdin.readline

k = int(input())

stack = []
sum = 0

for _ in range(k):
  num = int(input())
  if (num == 0):
    stack.pop()
  else:
    stack.append(num)

while stack:
  sum += stack.pop()

print(sum)
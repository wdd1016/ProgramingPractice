import sys
input = sys.stdin.readline

n = int(input())

stack1 = list(map(int, input().split()))
stack1.reverse()
stack2 = []
i = 1

while stack1:
  if stack1[-1] == i:
    i += 1
    stack1.pop()
  elif stack2 and stack2[-1] == i:
    i += 1
    stack2.pop()
  else:
    stack2.append(stack1.pop())

while stack2:
  if stack2[-1] != i:
    print("Sad")
    break
  else:
    stack2.pop()
    i += 1

if (i == n + 1):
  print("Nice")

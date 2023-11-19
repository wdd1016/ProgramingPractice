import sys
input = sys.stdin.readline

def findPrintNum(lst, start_idx, remain_count, printlst):
  if (remain_count == 0):
    print(*printlst)
    return
  remain_count -= 1
  for i in range(len(lst) - start_idx - remain_count):
    newprintlst = printlst.copy()
    newprintlst.append(lst[start_idx])
    start_idx += 1
    findPrintNum(lst, start_idx, remain_count, newprintlst)

n ,m = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()
printlst = []
findPrintNum(numbers, 0, m, printlst)
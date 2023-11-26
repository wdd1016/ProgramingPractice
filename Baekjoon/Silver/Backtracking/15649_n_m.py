import sys
import copy

input = sys.stdin.readline


def find_sequence(lst, n, m):
    if len(lst) == m:
        print(*lst)
        return
    for i in range(1, n + 1):
        if i not in lst:
            newlst = copy.deepcopy(lst)
            newlst.append(i)
            find_sequence(newlst, n, m)


n, m = map(int, input().split())
lst = []
find_sequence(lst, n, m)

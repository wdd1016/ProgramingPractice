import sys

input = sys.stdin.readline


def dfs(lst: list, numbers, visited, n, m):
    if len(lst) == m:
        print(*lst)
        return
    else:
        for i in range(n):
            if visited[i] == True:
                continue
            lst.append(numbers[i])
            visited[i] = True
            dfs(lst, numbers, visited, n, m)
            del lst[-1]
            visited[i] = False


n, m = map(int, input().split())
numbers = list(map(int, input().split()))
visited = [False for _ in range(n)]
numbers.sort()

lst = []
dfs(lst, numbers, visited, n, m)

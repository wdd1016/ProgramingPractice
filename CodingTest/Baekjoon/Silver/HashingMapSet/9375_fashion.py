import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dic = dict()
    for _ in range(n):
        wear, type_wear = input().rstrip().split()
        if type_wear in dic:
            dic[type_wear] += 1
        else:
            dic[type_wear] = 1
    answer = 1
    for count in dic.values():
        answer *= count + 1
    print(answer - 1)

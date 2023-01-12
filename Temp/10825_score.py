n = int(input())
lstcal = []
for i in range(n):
    lst = list(input().split())
    for j in range(1, 4):
        lst[j] = int(lst[j])
    lstcal.append(tuple(lst))
lstcal.sort(key = lambda x :(-x[1], x[2], -x[3], x[0]))
for i in range(n):
    print(lstcal[i][0])
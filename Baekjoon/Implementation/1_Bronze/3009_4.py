import sys
input = sys.stdin.readline

lst = []
lst += [list(map(int, input().split()))]
lst += [list(map(int, input().split()))]
lst += [list(map(int, input().split()))]
if (lst[0][0] == lst[1][0]):
	result = lst[2][0]
elif (lst[0][0] == lst[2][0]):
	result = lst[1][0]
else:
	result = lst[0][0]

if (lst[0][1] == lst[1][1]):
	result2 = lst[2][1]
elif (lst[0][1] == lst[2][1]):
	result2 = lst[1][1]
else:
	result2 = lst[0][1]
	
print(result, result2)
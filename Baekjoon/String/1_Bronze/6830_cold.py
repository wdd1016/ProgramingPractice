import sys
input = sys.stdin.readline

lst = []
while True:
	try:
		temp = list(input().split())
		temp[1] = int(temp[1])
		lst.append(temp)
	except:
		lst.sort(key=lambda x:x[1])
		print(lst[0][0])
		break
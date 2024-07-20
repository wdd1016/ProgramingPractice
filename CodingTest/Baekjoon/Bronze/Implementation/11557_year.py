t = int(input())
for i in range(t):
	n = int(input())
	lstn = []
	lstc = []
	for j in range(n):
		str1, str2 = input().split()
		lstn.append(str1)
		lstc.append(int(str2))
	print(lstn[lstc.index(max(lstc))])
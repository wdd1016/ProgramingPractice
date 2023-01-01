import sys
input = sys.stdin.readline

string = input().strip()
ln = len(string)
stra = "abcdefghijklmnopqrstuvwxyz"
strla = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
max = 0
isdup = 0

for i in range(26):
	count = string.count(stra[i])
	count += string.count(strla[i])
	if (count > max):
		max = count
		maxch = strla[i]
		isdup = 0
	elif (count == max):
		isdup += 1

if (isdup > 0):
	print("?")
else:
	print(maxch)

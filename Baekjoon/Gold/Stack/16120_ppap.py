import sys
input = sys.stdin.readline

lst = []
ppap = ["P","P","A","P"]
str1 = input().strip()
for i in range(len(str1)):
	lst.append(str1[i])
	while lst[-4:] == ppap:
		for _ in range(3):
			lst.pop()

if lst == ['P']:
	print("PPAP")
else:
	print("NP")
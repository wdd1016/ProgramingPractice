import sys
input = sys.stdin.readline

n = int(input())
str1 = input().strip()

result = ""
lst = ["000000", "001111", "010011", "011100", \
"100110", "101001", "110101", "111010"]
alpha = "ABCDEFGH"

def findword(temp):
	for i in range(8):
		count = 0
		for j in range(6):
			if (temp[j] == lst[i][j]):
				count += 1
		if (count >= 5):
			return alpha[i]
	return 'Z'

for i in range(n):
	char = findword(str1[6 * i : 6 * (i + 1)])
	if (char == 'Z'):
		print(i + 1)
		break
	else:
		result += char
if (char != 'Z'):
	print(result)
import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
for i in range(len(str2)):
	if str1.count(str2[i]) > 0:
		count += str1.count(str2[i])
print(len(str1) - count)
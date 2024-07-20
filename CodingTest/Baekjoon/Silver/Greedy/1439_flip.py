str1 = input()
len1 = len(str1)
flag = str1[0]
count = 0

for i in range(len1):
	if (str1[i] != str1[0] and str1[i] != flag):
		count += 1
	flag = str1[i]

print(count)
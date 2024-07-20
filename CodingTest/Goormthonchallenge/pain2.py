import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1000000)

# def minCount(num, cnt, a, b):
# 	if num < a:
# 		return -1
# 	elif cnt[num] == -1:
# 		return -1
# 	elif cnt[num] != 0:
# 		return cnt[num]
# 	elif num > b:
# 		tmp1 = minCount(num - a, cnt, a, b)
# 		tmp2 = minCount(num - b, cnt, a, b)
# 		if tmp1 == -1 and tmp2 == -1:
# 			cnt[num] = -1
# 		elif tmp1 == -1:
# 			cnt[num] = tmp2 + 1
# 		elif tmp2 == -1:
# 			cnt[num] = tmp1 + 1
# 		else:
# 			cnt[num] = min(tmp1, tmp2) + 1
# 	elif num > a:
# 		tmp1 = minCount(num - a, cnt, a, b)
# 		if tmp1 == -1:
# 			cnt[num] = -1
# 		else:
# 			cnt[num] = tmp1 + 1
# 	return cnt[num]

n = int(input())

a, b = map(int, input().split())

cnt = [-1 for _ in range(n+1)]

if (n == a or n == b):
	print(1)
elif (n < b and n % a == 0):
	print(n // a)
elif (n < b):
	print(-1)
else:
	cnt[a] = 1
	cnt[b] = 1
	for i in range(b+1, n+1):
		if cnt[i-a] == -1 and cnt[i-b] == -1:
			cnt[i] = -1
		elif cnt[i-a] == -1:
			cnt[i] = cnt[i-b] + 1
		elif cnt[i-b] == -1:
			cnt[i] = cnt[i-a] + 1
		else:
			if (cnt[i-a] < cnt[i-b]):
				cnt[i] = cnt[i-a] + 1
			else:
				cnt[i] = cnt[i-b] + 1
	print(cnt[n])

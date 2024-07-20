import sys
input = sys.stdin.readline

k = int(input())
if k < 0:
	k = -k
if k == 0:
	print(0)
elif k % 2 == 0:
	print(-1)
else:
	count = 0
	while k > 0:
		count += 1
		k = k // 2
	print(count)

https://seokgukim.github.io/2021/09/09/08-%EB%B0%B1%EC%A4%80-22973%EB%B2%88-%EC%A0%90%ED%94%84-%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88.html
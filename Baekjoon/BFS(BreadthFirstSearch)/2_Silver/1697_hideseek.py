from collections import deque

n, k = map(int, input().split())
arr = [0] * 100002

def bfs():
	card = deque()
	card.append(n)

	while card:
		x = card.popleft()
		if x == k:
			print(arr[x])
			break
		for y in (x-1, x+1, x*2):
			if y >= 0 and y <= 100000 and not arr[y]:
				arr[y] = arr[x] + 1
				card.append(y)

bfs()

# https://blog.naver.com/twonkang00/222661309664?isInf=true
# https://gmlwjd9405.github.io/2018/08/15/algorithm-bfs.html
# https://velog.io/@gnwjd309/python-queue
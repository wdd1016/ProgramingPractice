import sys, math
input = sys.stdin.readline

n = int(input())
lst = [0 for _ in range(10)]

while (n > 0):
	listn = list(map(int, str(n)))
	nlen = len(str(n))
	powers = nlen - 1
	downpowers = powers - 1
	firdigit = listn[0]
	nextnumber = n % (10 ** powers)
	for i in range(10):
		if n < 10: # 10미만은 해당 숫자들 count (0 제외)
			if i != 0 and i <= n:
				lst[i] += 1
# ex) 22343 -> 1~9999, 10000~19999, (20000~22343, 맨앞 2빼먹기 + '0' 4개)
		elif (i == 0 and max(lst) == 0): # 0은 앞에 숫자가 있어야 count되므로 맨처음 1번은 따로 계산
			lst[i] += ((10 ** downpowers) * powers) * (firdigit - 1) + powers # 마지막 더하기 power는 '20000의 4개'
			temp = 0
			for j in range(powers):
				temp += ((10 ** (downpowers - j)) - 1) * (10 ** j)
# 앞의 숫자가 모두 0인경우 1가지는 제외 (끝부터 10^3 - 1, (10^2 - 1) * (10^1), (10^1 - 1) * (10^2), ...)
			lst[i] += temp
		else:
			if (i == firdigit):
				lst[i] += nextnumber + 1
			elif (i < firdigit):
				if (i == 0):
					lst[i] += 10 ** powers - 1 # -1은 00부분 생각 (위에서 이미 더해줌)
				else:
					lst[i] += 10 ** powers		
			lst[i] += ((10 ** downpowers) * powers) * firdigit
# 만약 20450같이 앞의 자리를 빼면 0이되버려서 450이되면 큰일 (20000 ~ 20450에서 앞쪽의 0 count가 줄어듬)
		if (i == 0 and n > 100 and listn[1] == 0):
			k = 1
			while (k < nlen and listn[k] == 0):
				lst[0] += nextnumber
				k += 1
	n = nextnumber

print(*lst)

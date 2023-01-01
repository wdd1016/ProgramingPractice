import sys
input = sys.stdin.readline

x = int(input())
temp = x
num = 0 # num은 몇번째 라인(대각선)인지 확인

while temp > 0: # temp는 위치
	num += 1
	temp -= num

if (num % 2 == 0):
	print("%d/%d" % (num + temp, 1 - temp))
else:
	print("%d/%d" % (1 - temp, num + temp))
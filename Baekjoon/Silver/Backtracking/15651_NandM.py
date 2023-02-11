import sys
input = sys.stdin.readline

def sequence(n, m, depth, string, add):
	if (depth == m):
		string += str(add)
		print(string)
	else:
		string = string + str(add) + ' '
		for i in range(1, n+1):
			sequence(n, m, depth+1, string, i)

n, m = map(int, input().split())
newstring = ""
for k in range(1, n+1):
	sequence(n, m, 1, newstring, k)
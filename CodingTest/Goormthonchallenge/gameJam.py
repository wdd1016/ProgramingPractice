import sys
input = sys.stdin.readline

def move(info, direction, count, boardmap):
	for _ in range(count):
		if direction == 'U':
			if info[0] == 0:
				info[0] = n - 1
			else:
				info[0] -= 1
		elif direction == 'D':
			if info[0] == n - 1:
				info[0] = 0
			else:
				info[0] += 1
		elif direction == 'L':
			if info[1] == 0:
				info[1] = n - 1
			else:
				info[1] -= 1
		elif direction == 'R':
			if info[1] == n - 1:
				info[1] = 0
			else:
				info[1] += 1
		if boardmap[info[0]][info[1]] == 1:
			info[2] = False
			return
		else:
			boardmap[info[0]][info[1]] = 1
	return

n = int(input())

gmap = [[0 for _ in range(n)] for _ in range(n)]
pmap = [[0 for _ in range(n)] for _ in range(n)]

rg, cg = map(int, input().split())
ginfo = [rg-1, cg-1, True] 
rp, cp = map(int, input().split())
pinfo = [rp-1, cp-1, True]

gmap[ginfo[0]][ginfo[1]] = 1
pmap[pinfo[0]][pinfo[1]] = 1

commandmap = []
for i in range(n):
	commandmap += [list(input().split())]


while (ginfo[2]):
	move(ginfo, commandmap[ginfo[0]][ginfo[1]][-1], int(commandmap[ginfo[0]][ginfo[1]][:-1]), gmap)

while (pinfo[2]):
	move(pinfo, commandmap[pinfo[0]][pinfo[1]][-1], int(commandmap[pinfo[0]][pinfo[1]][:-1]), pmap)

gpoint = 0
ppoint = 0
for i in range(n):
	gpoint += gmap[i].count(1)
	ppoint += pmap[i].count(1)

if (gpoint > ppoint):
	print("goorm", gpoint)
else:
	print("player", ppoint)

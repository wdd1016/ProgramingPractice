count = 0

while True:
	try:
		a = input()
		count += 1

	except: 
		EOFError
		print(count)
		break

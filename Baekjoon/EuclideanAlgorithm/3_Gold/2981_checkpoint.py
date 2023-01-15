import sys
input = sys.stdin.readline

def find_gcd(num1, num2):
	if num1 < num2:
		num1, num2 = num2, num1
	while (num2):
		temp = num1 % num2
		num1 = num2
		num2 = temp
	return num1

n = int(input())
lst = []
for _ in range(n):
	lst.append(int(input()))
lst.sort()
lstsub = []
for i in range(n-1):
	lstsub.append(lst[i+1] - lst[i])
gcd = lstsub[0]
for i in range(1, n-1):
	gcd = find_gcd(gcd, lstsub[i])

gcdroot = int(gcd ** 0.5) + 1
lstprint = [gcd]
if (gcd > 3):
	for i in range(2, gcdroot):
		if (gcd % i == 0):
			if (gcd == i*i):
				lstprint.append(i)
			else:
				lstprint.extend([i, gcd//i])
lstprint.sort()

print(*lstprint)

# A = M * a + R
# B = M * b + R
# C = M * c + R
# 이렇게 둬보자.(문제 조건에 부합하는 식, M으로 각 수를 나눴을 때 나머지가 모두 같다)

# B - A = M(b-a)
# C- B = M(c-b)

# 이런 원리로, A~Z까지 입력받은 모든 수에 대해(오름차순), M은 B - A, C -B, ..., Z - Y의 공약수들이다.
# 즉, 이웃한 것끼리 뺀 수들의 최대공약수의, 1을 제외한 모든 약수가 M이 될 수 있는 것이다.
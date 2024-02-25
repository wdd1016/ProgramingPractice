import sys, math

input = sys.stdin.readline

m, n = map(int, input().split())

prime_state = [True for _ in range(n + 1)]
prime_state[0] = False
prime_state[1] = False

for i in range(int(math.sqrt(n)) + 1):
    if prime_state[i] == True:
        j = 2
        while i * j <= n:
            prime_state[i * j] = False
            j = j + 1

for num in range(m, n + 1):
    if prime_state[num] == True:
        print(num)

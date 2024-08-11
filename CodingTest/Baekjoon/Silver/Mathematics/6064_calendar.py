import sys

input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    lcm = m * n // gcd(m, n)
    ans = x
    if y == n:
        y = 0
    while ans <= lcm:
        if ans % n == y:
            print(ans)
            break
        else:
            ans += m
    if ans > lcm:
        print(-1)

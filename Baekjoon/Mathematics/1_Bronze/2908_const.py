import sys
input = sys.stdin.readline

a, b = input().strip().split()
rev_a = int(a[::-1])
rev_b = int(b[::-1])
print(max(rev_a, rev_b))
a = int(input())
b = int(input())
sum = 0

while b > 0 :
    sum += b % 10
    b = b // 10

print(sum)

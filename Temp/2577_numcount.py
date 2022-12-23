a = int(input())
b = int(input())
c = int(input())

k = a * b * c
lst = []
if k == 0:
    lst.append(0)
while k > 0:
    lst.append(k % 10)
    k = k // 10

for i in range(10):
    print(lst.count(i))

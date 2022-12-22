lst = list(map(int, input().split()))

for i in range(1,7):
  if lst.count(i) == 3:
    print(10000 + i * 1000)
    break;
  if i == 6:
    for j in range(1,7):
      if lst.count(j) == 2:
        print(1000 + j * 100)
        break;
      if j == 6:
        for k in range(6, 0, -1):
          if lst.count(k) == 1:
            print(k * 100)
            break;
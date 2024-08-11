import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n = input().rstrip().split()
    if m == "1":
        nums = list(map(int, n.split(sep=".")))
        answer = 0
        for i in range(len(nums)):
            answer = answer * 256 + nums[i]
        print(answer)
    else:
        num = int(n)
        nums = []
        if num == 0:
            nums.append(0)
        while num > 0:
            nums.append(num % 256)
            num = num // 256
        while len(nums) < 8:
            nums.append(0)
        nums.reverse()
        for i in range(8):
            if i != len(nums) - 1:
                print(nums[i], end="")
                print(".", end="")
            else:
                print(nums[i])

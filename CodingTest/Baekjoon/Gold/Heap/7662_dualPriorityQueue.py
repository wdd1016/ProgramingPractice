import sys, heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    minQ = []
    maxQ = []
    nums = dict()
    k = int(input())

    for _ in range(k):
        op, n = input().rstrip().split()
        n = int(n)

        if op == "I":
            if n in nums:
                nums[n] += 1
            else:
                nums[n] = 1
                heapq.heappush(minQ, n)
                heapq.heappush(maxQ, -n)
        elif op == "D":
            if len(nums) != 0:
                if n == -1:
                    while minQ[0] not in nums:
                        heapq.heappop(minQ)
                    nums[minQ[0]] -= 1
                    if nums[minQ[0]] == 0:
                        del nums[minQ[0]]
                elif n == 1:
                    while -maxQ[0] not in nums:
                        heapq.heappop(maxQ)
                    nums[-maxQ[0]] -= 1
                    if nums[-maxQ[0]] == 0:
                        del nums[-maxQ[0]]
    if len(nums) == 0:
        print("EMPTY")
    else:
        while minQ[0] not in nums:
            heapq.heappop(minQ)
        while -maxQ[0] not in nums:
            heapq.heappop(maxQ)
        print(-maxQ[0], minQ[0])

import sys
input = sys.stdin.readline

def printnumber(k, start, lst, nums):
	if (len(nums) == 6):
		print(*nums)
	else:
		for i in range(start, k):
			nums2 = nums.copy()
			nums2.append(lst[i])
			if (len(nums2) != len(set(nums2))):
				break
			printnumber(k, i + 1, lst, nums2)
	return

while (True):
	lst = list(map(int, input().split()))
	if lst == [0]:
		break
	k = lst.pop(0)
	nums = []
	printnumber(k, 0, lst, nums)
	print()

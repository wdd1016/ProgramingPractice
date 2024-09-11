import sys

input = sys.stdin.readline

# def binarySearch(sortedArray, value):
#     low = 0
#     high = len(sortedArray) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if sortedArray[mid] == value:
#             return mid
#         elif sortedArray[mid] > value:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1


# n = int(input())
# holes = list(map(int, input().split()))

# q = int(input())
# acorns = list(map(int, input().split()))

# arranged_acorns = sorted(acorns)
# arranged_answer = [0 for _ in range(q)]

# j = 0
# for i in range(q):
#     while holes[j] < arranged_acorns[i] - j:
#         j += 1
#     arranged_answer[i] = j + 1

# answer = [0 for _ in range(q)]
# for i in range(q):
#     idx = binarySearch(arranged_acorns, acorns[i])
#     answer[i] = arranged_answer[idx]

# print(*answer)

n = int(input())
holes = list(map(int, input().split()))
for i in range(n):
    holes[i] += i

q = int(input())
acorns = list(map(int, input().split()))

max_acorn_size = max(acorns)
acorn_hole_num_by_size = [0 for _ in range(max_acorn_size + 1)]

acorn_size = 1
for i in range(n):
    while acorn_size <= holes[i] and acorn_size <= max_acorn_size:
        acorn_hole_num_by_size[acorn_size] = i + 1
        acorn_size += 1

answer = [acorn_hole_num_by_size[acorns[i]] for i in range(q)]

print(*answer)

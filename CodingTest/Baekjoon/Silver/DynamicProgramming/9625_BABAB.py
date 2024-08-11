import sys

input = sys.stdin.readline

k = int(input())

# string = "A"

# for _ in range(k):
#     newString = ""
#     for char in string:
#         if char == "A":
#             newString += "B"
#         else:
#             newString += "BA"
#     string = newString

acount = 1
bcount = 0

# for ch in string:
#     if ch == "A":
#         acount += 1
#     else:
#         bcount += 1

for _ in range(k):
    previousBcount = bcount
    bcount = acount + previousBcount
    acount = previousBcount

print(acount, end=" ")
print(bcount)

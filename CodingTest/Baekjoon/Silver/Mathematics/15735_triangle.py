import sys

input = sys.stdin.readline

n = int(input())

count = 0

# 시간초과
# for i in range(1, n + 1):  # 몇 층인가?
#     for j in range(1, i + 1):  # 길이가 몇 인 삼각형을 세는가?
#         total_number = i - j + 1  # 해당 길이의 삼각형이 그 층에 몇 개 있는가?
#         count += total_number  # 상방으로의 삼각형
#         if i + j <= n:  # 만약 하방으로의 삼각형이 가능하다면
#             count += total_number  # 더한다.

for i in range(1, n + 1):  # 길이가 i인 삼각형을 구해보자.
    # 등차수열
    total_upper_floor_number = n - i + 1  # 상방으로의 삼각형 밑변 층 수
    final_upper_term = n - i + 1  # 가장 밑 바닥에서의 상방 삼각형 수
    count += (total_upper_floor_number * (1 + final_upper_term)) // 2

    total_lower_floor_number = n - 2 * i + 1  # 하방으로의 삼각형 밑변 층 수
    if total_lower_floor_number > 0:
        final_lower_term = n - 2 * i + 1  # 가장 밑 바닥 + i 에서의 하방 삼각형 수
        count += (total_lower_floor_number * (1 + final_lower_term)) // 2

print(count)

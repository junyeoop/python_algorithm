import sys

sys.stdin = open("input.txt", "r")


def max_sub_array(arr, k):
    window_sum = 0
    max_sum = 0
    window_start = 0
    save = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # 슬라이딩 인덱스 범위 요소 합산

        # 슬라이딩 윈도우의 범위가 k 보다 커진 경우
        if window_end >= (k - 1):
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]  # 슬라이드 윈도우 범위를 벗어난 요소를 합계에서 제거
            save = window_start

            window_start += 1  # 슬라이드 윈도우 시작 인덱스 증가

    return save

n, t = map(int, input().split())
# schedule = [[] for _ in range(n)]
schedule = []
for _ in range(n):
    # time_number = int(input())
    for _ in range(int(input())):
        schedule.append(list(map(int, sys.stdin.readline().split())))

print(schedule)
time = [0 for _ in range(100000)]
for start, end in schedule:
    time[start] += 1
    time[end] += -1
# print(time)

for i in range(len(time)):
    if i == 0:
        continue
    time[i] = time[i - 1] + time[i]
# print(time)
# m = 0
# iz = 0
# for i in range(24 - t):
#     result = 0
#     print(i)
#     for j in range(t):
#         result += time[i + j]
#         # print(i + j)
#     if result > m:
#         m = result
#         iz = i
#     # print("")
iz = max_sub_array(time, t)
print(iz, iz + t)

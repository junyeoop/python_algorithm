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
            if window_sum > max_sum:    # 슬라이드 윈도우의 총합이 max_sum 초과일때 윈도우 시작점 저장
                save = window_start
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]  # 슬라이드 윈도우 범위를 벗어난 요소를 합계에서 제거
            window_start += 1  # 슬라이드 윈도우 시작 인덱스 증가

    return save


n, t = map(int, sys.stdin.readline().split())
schedule = []
time = [0 for _ in range(100100)]
m = 0
index = 0

for _ in range(n):
    for _ in range(int(sys.stdin.readline())):
        schedule.append(list(map(int, sys.stdin.readline().split())))

for start, end in schedule:
    # print(f'time,start: {time[start]}, time,end: {time[end]}')
    # start, end = int(schedule[i][0]), int(schedule[i][1])
    time[start] += 1
    time[end] -= 1

for i in range(1, len(time)):
    time[i] = time[i - 1] + time[i]

# for i in range(len(time) - t):
#     result = 0
#     for j in range(t):
#         result += time[i + j]
#         # print(i + j)
#     if result > m:
#         m = result
#         index = i
index = max_sub_array(time, t)
print(index, index + t)

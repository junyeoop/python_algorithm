import sys
import collections

INF = sys.maxsize


# nums, 슬라이딩 윈도우 값 k가 주어졌을때 -> 슬라이딩 윈도우 안의 max값을 누적한 List 반환
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    result = []
    window = collections.deque()
    current_max = -INF

    for i, v in enumerate(nums):
        window.append(v)
        if i < k - 1:
            continue

        # 새로 추가된 값이 최댓값보다 큰 경우 교체
        if current_max == -INF:
            current_max = max(window)
        elif v > current_max:
            current_max = v

        result.append(current_max)

        # 최댓값이 윈도우에서 빠지면 초기화
        if current_max == window.popleft():
            current_max = -INF


def maxSlidingWindow_low_efficient(nums: list[int], k: int) -> list[int]:
    if not nums:
        return nums

    r = []
    for i in range(len(nums) - k + 1):
        r.append(max(nums[i:i + k]))

    return nums

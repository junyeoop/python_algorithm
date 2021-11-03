import bisect

def binary_search(left, right, target):
    if left <= right:
        # 이게 안전한 방법
        mid = left + (right - left) // 2

        # 이건 보통 우리가 쓰는 방법,자료형의 최댓값 초과하면(overflow) 에러 발생생
        # mid  (left + right) // 2
        if mid < target:
            return binary_search(mid + 1, right)
        elif mid > target:
            return binary_search(mid + 1, right)
        else:  # mid == target
            return mid

    else:  # 범위 넘어감
        return -1


def binary_search_iterative(left, right, target):

    while left <= right:
        # 이게 안전한 방법
        mid = left + (right - left) // 2

        # 이건 보통 우리가 쓰는 방법,자료형의 최댓값 초과하면(overflow) 에러 발생생
        # mid  (left + right) // 2
        if mid < target: # mid ----- target ----- right
            left = mid + 1
        elif mid > target: # left ----- target ----- mid
            right = mid - 1
        else:  # mid == target
            return mid

# 검색 모듈 : bisect
index = bisect.bisct_left()
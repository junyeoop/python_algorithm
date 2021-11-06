def solution(numbers, target):
    length = len(numbers)
    # visited=[False]*length
    count = 0
    answer = 0

    def dfs(idx, result):
        # visited[v] = True

        if (idx == length):
            if result == target:
                nonlocal answer
                answer += 1
                return answer
            return

        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])

    dfs(0, 0)

    return answer

###############################################################################################################

def solution2(numbers, target):
    length = len(numbers)
    # visited=[False]*length
    count = 0
    answer = 0

    def dfs(idx, result):
        # visited[v] = True

        if (idx == length):
            if result == target:
                nonlocal answer
                answer += 1
                return answer
            return

        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])

    dfs(0, 0)

    return answer

###############################################################################################################

def solution3(numbers, target):
    length = len(numbers)
    # visited=[False]*length
    count = 0
    answer = 0

    def dfs(idx, result):
        # visited[v] = True

        if (idx == length):
            if result == target:
                nonlocal answer
                answer += 1
                return answer
            return

        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])

    dfs(0, 0)

    return answer
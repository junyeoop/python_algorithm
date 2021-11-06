import bisect


# 사람 제한 없이 푼 문제...하하..
def solution(people, limit):
    answer = 0
    n = len(people)
    people.sort(reverse=True)
    # print(people)

    saved = [1 for _ in range(n)]

    while sum(saved):
        w = limit
        for i in range(n):
            if saved[i] == 0:
                continue
            else:
                if w < people[-1]:
                    break
                if people[i] <= w:
                    saved[i] = 0
                    w -= people[i]

        answer += 1

    return answer


# 투포인터 활용
def solution2(people, limit):
    answer = 0
    n = len(people)
    people.sort()
    min_idx = 0
    max_idx = n - 1

    while min_idx <= max_idx:
        if min_idx == max_idx:
            answer += 1
            break
        else:
            if people[min_idx] + people[max_idx] <= limit:
                answer += 1
                min_idx += 1
                max_idx -= 1

            else:
                max_idx -= 1
                answer += 1

    return answer


print('답 :', solution2([20, 50, 50, 80], 100))

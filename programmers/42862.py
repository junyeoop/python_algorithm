def solution(n, lost, reserve):
    intersection = list(set(lost) & set(reserve))  # 교집합 구하기

    lost = list(set(lost) - set(intersection))
    reserve = list(set(reserve) - set(intersection))

    # for i in lost:
    # if i in reserve:
    #  answer += 1
    #   reserve.remove(i)
    #  lost.remove(i)
    # print(f'{i} 번호 실행, 내꺼 2개 가져옴, {lost}, {reserve}')

    # print(lost)
    # print(reserve)

    answer = n - len(lost)
    for i in lost:
        if i - 1 in reserve:
            answer += 1
            reserve.remove(i - 1)
            continue

        if i + 1 in reserve:
            answer += 1
            reserve.remove(i + 1)
            continue

    return answer

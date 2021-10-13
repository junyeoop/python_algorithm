import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("input.txt", "r")


def is_palindrome(s):
    #print(s)
    return s == s[::-1]


# 입력
for test_case in range(1, 11):
    count = 0
    input_map = []
    length = int(input())
    # map_a = [input() for _ in range(8)]
    # print(map_a)
    for _ in range(8):
        input_map.append(list(map(str, input().split())))


    #print(length, '길이')
    #print(input_map)
    count =0

    #가로
    for i in range(8):
        for j in range(8 - length + 1):
            if is_palindrome(input_map[i][0][j:j+length]):
                #print(input_map[i][0][j:j+length])
                count += 1

    #세로
    for i in range(8):
        for j in range(8-length+1):
            target = ''
            for k in range(length):
                target += (input_map[j+k][0][i])
            if is_palindrome(target):
                #(target)
                count += 1
    print(f'#{test_case} {count}')






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
    return s == s[::-1]


# 입력
for test_case in range(10):
    num = int(input())
    input_map = [input() for _ in range(100)]
    input_map_r = []
    length = 0
    str_p = ''

    #가로 세로 바꾸기
    for i in range(100):
        target = ''
        for j in range(100):
            target += input_map[j][i]
        input_map_r.append(target)
  
    # 가로
    for i in range(100):
        for j in range(100):
            for k in range(j, 101):
                if is_palindrome(input_map[i][j:k]):
                    length = max(length, k - j)

    # 세로
    for i in range(100):
        for j in range(100):
            for k in range(j, 101):
                if is_palindrome(input_map_r[i][j:k]):
                    length = max(length, k - j)
                    
    print(f'#{num} {length}')

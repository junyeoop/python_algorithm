#그래프 시작점 찾기

import sys
sys.stdin = open("input.txt", "r")

def up(row: int, index: int)-> int:
    while(True):
        if row == 0:
            return index
        if index < 99 and ladder[row][index+1]:
            while index < 99 and ladder[row][index+1]:
                index += 1
            else:
                row -= 1
        elif index > 0 and ladder[row][index-1]:
            while index > 0 and ladder[row][index-1]:
                index -= 1
            else:
                row -= 1
        else:
            row -= 1


for test_case in range(1, 11):
    test_case_num = int(input())
    ladder = []
    for i in range(100):
        ladder.append(list(map(int, input().split())))

    index = ladder[99].index(2)
    # print(ladder)
    # print(index)
    row = 99

    print(f'#{test_case} {up(row, index)}')

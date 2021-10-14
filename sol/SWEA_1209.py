import sys
sys.stdin = open("input.txt", "r")
for test_case in range(1, 11):
    a = int(input())
    imap = []
    for _ in range(100):
        imap.append(list(map(int, input().split())))
        # [input().split() for _ in range(100)]
    # print(imap[99][1])
    # print(imap[1])
    dia1, dia2, sum1, sum2 = 0, 0, 0, 0
    
    # 2차원 배열 행렬 바꾸기
    imap_r = list(map(list, zip(*imap)))

    print(imap_r[99][-1])
    # print(imap[99][1])
    for i in range(0, 100):
        dia1 += imap[i][i]
        dia2 += imap[i][99 - i]
        sum1 = max(sum1,sum(imap[i]))
        sum2 = max(sum2, sum(imap_r[i]))

    # for i in range(100):
    #     for j in range(100):

    # print(imap)
    result = max(dia1, dia2, sum1, sum2)
    print(f'#{test_case} {result}')

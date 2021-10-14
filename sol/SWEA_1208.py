for test_case in range(1, 11):
    count = int(input())
    imap = list(map(int, input().split()))
    imap.sort()
    # hmax = 0
    # hmin = 100

    for i in range(count):
        imap[99] -= 1
        imap[0] += 1
        imap.sort()

    # for i in range(100):
    #     hmin = min(hmin, imap[i])
    #     hmax = max(hmax, imap[i])

    # 그냥 리스트에서 max(list)하면 되네..
    print(f'#{test_case} {max(imap) - min(imap)}')
    
    

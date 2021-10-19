for test_case in range(1, 11):
    count=0
    t_length = int(input())
    t_list = list(map(int,input().split()))

    for i in range(2, t_length-2):
        height = max(t_list[i-2], t_list[i-1], t_list[i+1], t_list[i+2])
        if t_list[i] > height:
            count+=(t_list[i]-height)

    print(f'#{test_case} {count}')

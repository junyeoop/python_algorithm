import sys

sys.stdin = open("sample_input.txt", "r")

dx = [+1, +1, -1, -1, 0]
dy = [-1, +1, +1, -1, 0]


def dfs(x, y, dir, visited_num):
    # print (dir)
    global R
    # 방향 4번 이상 바꾸면 False
    if dir >= 4:
        return False

    x += dx[dir]
    y += dy[dir]

    # 맵 벗어나는 경우 False
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if (x, y) == (j, i):
        if len(visited_num) > R:
            R = len(visited_num)
        return

    # 이미 먹었던 디저트인 경우 False
    if graph[x][y] in visited_num:
        return False

    # if visited[x][y] == 0:
    #     # 왔던 거 체크
    #     visited[x][y] = 1

    # 먹었던 종류 삽입
    visited_num.append(graph[x][y])

    dfs(x, y, dir, visited_num)
    dfs(x, y, dir + 1, visited_num)
    visited_num.pop()
    # visited_num.pop()
    # return True
    # visited[x][y] = 0

    # 이미 들렀던 곳이면 false / visited[x][y] == 1


T = int(input())
for T in range(T):
    answer = -1
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    R = -1
    for i in range(n):
        for j in range(n):
            visited = [[0] * n for _ in range(n)]
            visited_num = list([graph[j][i]])
            dir = 0
            dfs(j, i, dir, visited_num)
            if len(visited_num) > answer:
                pass
                # print(visited_num)
                # print(i, j)

                # for a in visited:
                #     for b in a:
                #         print(b, end=" ")
                #     print()
                # print()
            answer = max(answer, R)

    # print(graph)

    print(f'#{T + 1} {answer}')

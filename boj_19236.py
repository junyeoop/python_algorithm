import collections
import sys
import copy

# sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")

# dx = [0, -1, -1, 0, +1, +1, +1, 0, -1]
# dy = [0, 0, -1, -1, -1, 0, +1, +1, +1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

graph = [[None] * 4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))

    for j in range(4):
        graph[i][j] = [data[2 * j], data[2 * j + 1] - 1]

# def turn_left(dir):
#     dir = ((dir) % 9)
#     if dir == 0:
#         dir =1
#     return dir
def turn_left(direction):
    return (direction + 1) % 8


def find_fish(index):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == index:
                return (i, j)
    return None


def change_fish(graph, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(i)
        if position is None:
            continue
        else:
            x, y = position[0], position[1]
            dir = graph[x][y][1]

            for j in range(8):
                nx = x + dx[dir]
                ny = y + dy[dir]

                # if nx >= 4 or nx < 0 or ny >= 4 or ny < 0:
                #     dir = turn_left(dir)
                # else:
                #     if graph[nx][ny][0] != -1:
                #         graph[nx][ny][1] = dir
                #         graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]
                #         break
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == now_x and ny == now_y):
                        graph[nx][ny][1] = dir
                        graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]
                        break
                dir = turn_left(dir)


def get_possible(now_x, now_y, dir):
    list = []

    for i in range(1, 5):
        nx = now_x + dx[dir]
        ny = now_y + dy[dir]

        if 0 <= nx < 4 and 0 <= ny < 4:
            if graph[nx][ny] != -1:
                list.append([nx, ny])
    return list

    # positions = []
    # direction = graph[now_x][now_y][1]
    # # 현재의 방향으로 쭉 이동하기
    # for i in range(4):
    #     now_x += dx[direction]
    #     now_y += dy[direction]
    #     # 범위를 벗어나지 않는지 확인하며
    #     if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4:
    #         # 물고기가 존재하는 경우
    #         if graph[now_x][now_y][0] != -1:
    #             positions.append((now_x, now_y))
    # return positions


# total = 0
result = 0


def dfs(graph, now_x, now_y, total):
    global result
    graph = copy.deepcopy(graph)
    total += graph[now_x][now_y][0]

    graph[now_x][now_y][0] = -1
    shark_dir = graph[now_x][now_y][1]

    change_fish(graph, now_x, now_y)

    possible_to_go = get_possible(now_x, now_y, shark_dir)

    if len(possible_to_go) == 0:
        # print(total)
        result = max(result, total)
        return

    for next in possible_to_go:
        nx, ny = next[0], next[1]
        dfs(graph, nx, ny, total)
    # for next_x, next_y in possible_to_go:
    #     dfs(graph, next_x, next_y, total)


# change_fish(graph)
# print(graph)
dfs(graph, 0, 0, 0)
print(result)

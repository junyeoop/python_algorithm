import collections
import sys

sys.stdin = open("input.txt", "r")

result = 0

# dir은 1 ~ 8 까지
dc = [-1, -1, 0, +1, +1, +1, 0, -1]
dr = [0, +1, +1, +1, 0, -1, -1, -1]


def move_cloud(r, c, di, si):
    cloud_r = r + (si * dr[di - 1])
    cloud_c = c + (si * dc[di - 1])

    cloud_c %= N
    cloud_r %= N
    if (cloud_c == 0):
        cloud_c = 5
    if (cloud_r == 0):
        cloud_r = 5

    # print(cloud_r, cloud_c, N)
    print(water[cloud_r][cloud_c])

    water[cloud_r][cloud_c] += 1
    watercopy(cloud_r, cloud_c)

    # water[cloud_r][cloud_c + 1] += 1
    # watercopy(cloud_r, cloud_c + 1)
    #
    # water[cloud_r - 1][cloud_c] += 1
    # watercopy(cloud_r - 1, cloud_c)
    #
    # water[cloud_r - 1][cloud_c + 1] += 1
    # watercopy(cloud_r - 1, cloud_c + 1)

    pass


def bibaragi(r, c, di, si):
    move_cloud(r, c, di, si)
    watercopy(r, c)
    pass


def watercopy(r, c):
    # UP, LEFT
    if r - 1 > 0 and c - 1 > 0 and water[r - 1][c - 1] > 0:
        water[r][c] += 1
    # UP, RIGHT
    if r - 1 > 0 and c + 1 <= N and water[r - 1][c + 1] > 0:
        water[r][c] += 1
    # DOWN, LEFT
    if r + 1 <= N and c - 1 > 0 and water[r + 1][c - 1] > 0:
        water[r][c] += 1
    # UP, LEFT
    if r + 1 <= N and c + 1 <= N and water[r + 1][c + 1] > 0:
        water[r][c] += 1


# main

N, M = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(N)]

# N개 입력받기
water = [[False] for i in range(N + 1)]
water[0] = [False for _ in range(N)]
for i in range(1, N + 1):
    water[i] += (list(map(int, input().split())))

input_data = [[] for i in range(M)]

# M개 입력받기
for i in range(M):

    input_data[i] = (list(map(int, input().split())))
#비바라기
clouds = collections.deque([[N, 1], [N, 2], [N - 1, 1], [N - 2, 2]])
# 실행
for m in range(M):
    di = input_data[m][0]
    si = input_data[m][1]

    c_length = len(clouds)

    # print(di, si)
    for _ in range(len(clouds)):
        cloud = clouds.popleft()
        print(cloud)
        move_cloud(cloud[0], cloud[1], di, si)


print(sum(sum(a) for a in water))
# print(len(water))


# https://chldkato.tistory.com/192 참고하자..
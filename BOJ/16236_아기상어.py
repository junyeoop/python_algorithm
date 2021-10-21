import collections
import sys

INF = sys.maxsize
sys.stdin = open("16236_input.txt", "r")

# 입력
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]



# 변수
shark_size = 2  # 상어 크기
shark_x, shark_y = 0, 0  # 상어의 현재위치
dx = [-1, 0, +1, 0]
dy = [0, 1, 0, -1]
count = 0 # 먹은 수
total_time = 0 # 걸린 시간, 결과

# 상어 찾고 초기화
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            graph[i][j] = 0

def bfs():
    # 최단 거리용 리스트
    global shark_x, shark_y

    dist = [[-1] * n for _ in range(n)]
    q = collections.deque([(shark_x, shark_y)])
    # print(dist)
    # print(shark_x, shark_y)
    dist[shark_x][shark_y] = 0

    # print(q)
    # print(type(q.popleft()))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                # dist[nx][ny] == -1은 이전까지는 도달할 수 없었지만, dist[x][y]에서 연결되어있으므로 가중치를 더해 새로 값을 업데이트한다.
                if dist[nx][ny] == -1 and graph[nx][ny] <= shark_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    # 최단 거리 테이블 반환
    return dist


def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달할 수 있는 곳이고, 물고기 존재하고, 물고기 크기가 상어보다 작다면,
            if dist[i][j] != -1 and 1 <= graph[i][j] and graph[i][j] < shark_size:
                # 제일 위, 제일 왼쪽 물고기 먹겠다.
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        # print("없어!")
        return None
    else:
        return x, y, min_dist


while True:
    z = bfs()
    tmp = find(bfs())

    if tmp is None:
        print(total_time)
        break
    else:
        shark_x, shark_y = tmp[0], tmp[1]
        total_time += tmp[2]

        graph[shark_x][shark_y] = 0
        count += 1

        if count >= shark_size:
            shark_size += 1
            count = 0

import sys

INF = sys.maxsize

# 노드 개수, 간선 개수
n, m = map(int, input().split())

# 시작 노드 번호 입력
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 / 리스트 개수를 n+1로 만들어서 인덱스랑 노드숫자랑 맞추기
graph = [[] for i in range(1, n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 노드에서 b노드로 가는데 걸리는 비용 c
    graph[a].append((b, c))


# 방문 x 노드 중, distance가 가장 짧은 노드 index 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True

    # 거리 테이블 업데이트
    for linked_data in graph[start]:
        # distance(연결된 도착 노드) = 거리값
        distance[linked_data[0]] = linked_data[1]

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True

        for data in graph[now]:
            cost = distance[now] + data[1]

            if cost < distance[data[0]]:
                distance[data[0]] = cost


dijkstra(start)

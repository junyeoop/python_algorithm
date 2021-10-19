'''
우선순위 큐 사용
visited 리스트 필요 x
'''

import heapq
import sys

INF = sys.maxsize

# 노드 개수, 간선 개수
n, m = map(int, input().split())

# 시작 노드 번호 입력
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 / 리스트 개수를 n+1로 만들어서 인덱스랑 노드숫자랑 맞추기
graph = [[] for i in range(1, n + 1)]
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 노드에서 b 노드로 가는데 걸리는 비용 c
    graph[a].append((b, c))


def dijkstra(start):
    '''우선순위 큐 쓸건데, 파이썬에서 heapq는 최소 힙이니까, 위 for 문에서 a, b, c로 입력받은거 순서 바꿀거야. (거리, 도착) 순으로. 그래야 거리 짧은거 먼저 pop되니까. get_shortest_node()가 필요 없어진다.'''
    queue = []
    heapq.heappush(queue, (0, start))

    distance[start] = 0

    # queue가 비어있지 않다면 진행
    while queue:
        # 최단 거리 노드 정보 꺼내기
        dist, now = heapq.heappop(queue)
        # 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 꺼낸 노드랑 연결된 노드정보들 순차적으로 확인
        for w in graph[now]:
            # w[1]은 거리
            cost = dist + w[1]
            if cost < distance[w[0]]:
                distance[w[0]] = cost
                # 새로운 값으로 바꿔서 도착점 업데이트
                heapq.heappush(queue, (cost, w[0]))


dijkstra(start)

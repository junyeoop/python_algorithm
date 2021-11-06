# import collections
import sys
import heapq


def solution(n, costs):
    stack = []

    path = []
    answer = 0
    min_save = sys.maxsize

    def dfs(start, path, visited):
        if len(path) == (n - 1):
            # print('이거 반환!', path)
            return path
        visited[start] = True
        print(start, end=' ')
        print(path)
        # path.append(data[start][2])
        for w in data[start]:
            # if len(path) == (n - 1):
            #     break
            if visited[w[0]] is False:
                # if len(path) == (n - 1):
                #     return path
                path.append(w[1])
                dfs(w[0], path, visited)
        return path

    data = [[] for _ in range(n)]

    # 입력값 분배
    for cost in costs:
        data[cost[0]].append([cost[1], cost[2]])
        data[cost[1]].append([cost[0], cost[2]])

    # print(*data, sep='\n')

    for i in range(n):
        path = []
        visited = [False for _ in range(n)]
        # print(data[i])
        print(f'\n{i}번 노드')
        result = dfs(i, path, visited)
        # print(f'{i}번 노드 결과 값 {result}')
        min_save = min(sum(result), min_save)

    print('\n', min_save)
    return min_save


def solution2(n, costs):
    INF = sys.maxsize
    min_save = sys.maxsize
    distance = [INF] * (n)
    data = [[] for _ in range(n)]

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
            for w in data[now]:
                # w[1]은 거리
                cost = dist + w[1]
                if cost < distance[w[0]]:
                    distance[w[0]] = cost
                    # 새로운 값으로 바꿔서 도착점 업데이트
                    heapq.heappush(queue, (cost, w[0]))

    # 입력값 분배
    for cost in costs:
        data[cost[0]].append((cost[1], cost[2]))
        data[cost[1]].append((cost[0], cost[2]))
    print(data)
    dijkstra(2)
    s = 0
    print(distance)
    for d in distance:
        if d != INF:
            s += d
    print(s)
    return s


def solution3(n, costs):
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)

        if a < b:
            parent[b] = a
        else:
            parent = b

    # 초기화 / 입력
    answer = 0
    m = len(costs)
    edges = []
    parent = [0] * (n)
    for i in range(n):
        parent[i] = i

    for cost in costs:
        edges.append((cost[2], cost[0], cost[1]))

    edges.sort()
    print(edges)
    for edge in edges:
        cost, a, b = edge

        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost

    return answer


solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
# solution2(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])

'''
TestCase

5 [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]] 15
5 [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]] 8
4 [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]] 9
5 [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]] 104
6 [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]] 11
5 [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]] 6
5 [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]] 8
5 [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]] 8
'''

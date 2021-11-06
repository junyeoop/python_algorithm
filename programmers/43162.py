def solution(n, computers):
    answer = []
    path = []
    visited = [0 for _ in range(n)]

    # print(visited)

    def dfs(start, path):
        if sum(computers[start]) == 1 and sum(visited) == n:
            if path not in answer:
                return answer.append(path)
        if visited[start] == 1:
            return

        visited[start] = 1
        path.append(start)
        # print(start, end=' ')

        for i in range(n):
            if computers[start][i] == 1 and visited[i] == 0 and i != start:
                # print(f'{i} 컴퓨터 방문')
                dfs(i, path)
        answer.append(path)

    count = 0
    i = 0

    # 여기가 포인트!
    while True:
        if 0 in visited:
            dfs(visited.index(0), path)
            i += 1
            count += 1
        else:
            break

    print(count)
    return count

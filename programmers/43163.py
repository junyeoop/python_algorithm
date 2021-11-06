import collections


def solution(begin, target, words):
    def bfs(begin, visited, answer):
        visited[begin] = True
        q = collections.deque([begin])

        while q:
            now = q.popleft()
            visited[now] = True

            if now == target:
                print("qqqqqqqq")
                print(answer)
                return answer
                break

            for i in range(n):
                if len(set(words[i]) - set(now)) == 1:
                    if visited[words[i]] == True:
                        continue
                    visited[words[i]] = True
                    print("!", words[i], visited[words[i]])
                    q.append(words[i])
            answer += 1

        return answer

    if target not in words:
        return 0

    answer = 0
    n = len(words)

    path = []
    visited = collections.defaultdict(bool)
    for word in words:
        visited[word] = False

    a = bfs(begin, visited, answer)

    return a
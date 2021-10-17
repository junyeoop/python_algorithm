# DFS 문제
import sys
sys.stdin = open("input.txt", "r")

import collections

def dfs(index):

    visited[index] = True
    stack.append(index)

    for w in graph[index]:
        if visited[w] == False:
            visited[w] = True
            # path.append(index)
            dfs(w)
    stack.pop()


for t in range(10):
    result = 0
    num, length = map(int, input().split())
    l = list(map(int, input().split()))
    graph = collections.defaultdict(list)
    visited = [False] * (100)
    stack = []
    #print(l)

    for i in range(0, len(l), 2):
        graph[l[i]].append(l[i+1])

    pathes = []

    dfs(0)
    #print(visited)
    if(visited[99] == True):
        result = 1
    #print(graph)
    print(f'#{t+1} {result}')

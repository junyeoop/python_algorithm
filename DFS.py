import collections

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

# 스택사용, 재귀보다 반복이 조금 더 빨라, 보통 BFS보다 DFS로 풀이

# 동작 과정 :
# 1. 탐색 시작 노드(v)를 스택에 삽입 후 방문 처리(discovered)
# 2. 스택 최상단 노드에 방문하지 않은 인접 노드 존재 -> 인접 노드를 스택에 삽입 후 방문 처리
# 3. 방문하지 않은 인접 노드 존재 x -> 스택의 최상단 노드 pop
# 4. 2~3 과정 반복


# recursive pseudocode
#  DFS(G,V)
#    label v as discovred
#    for all directed deges from v to w that are in G.adjacentEdges(v) do
#      if vertex w is not labeled as discovered then
#        recursively call DFS(G, w)


def recursiveDFS(v, discovered=[]):
    # 현재 노드 방문처리
    discovered.append(v)
    # 현재 노드와 연결된 다른 노드 방문
    for w in graph[v]:
        if not w in discovered:
            discovered = recursiveDFS(w, discovered)
    return discovered


# iterative pseudocode
# DFS-iterative(G,V)
#  let S be a satck
#  S.push(v)
#  while S in not empty do
#   v = S.pop()
#   if v si not labeled as discovered then
#     label v as discovered
#     for all edges from v to w in G.adjacnetEdges(v) do
#       S.push(w)
  
  
def stackDFS(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        vertex = stack.pop()
        if vertex not in discovered:
            discovered.append(vertex)
            for w in graph[vertex]:
                stack.append(w)
    return discovered


# recursiveDFS(1)
# stackDFS(1)

---------------------------------------------------------------------

def dfs(graph, v, visited)





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


# recursive pseudocode
#  DFS(G,V)
#    label v as discovred
#    for all directed deges from v to w that are in G.adjacentEdges(v) do
#      if vertex w is not labeled as discovered then
#        recursively call DFS(G, w)


def recursiveDFS(v, discovered=[]):
    discovered.append(v)
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

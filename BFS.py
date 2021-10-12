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

# 큐 사용, 재귀로 동작 불가

# iterative pseudocode

# BFS(G, start_v)
# let Q be a queue
# label start_v as discovered
# Q.enqueue(start_v)
# while Q is not empty do
#   v := Q.dequeue()
#   if v is the goal then
#     return V
#   for all edges from v to w in G.adjacentEdges(v) do
#     if w is no labeled as discovered then
#       label w as discovered
#       w.parent := v
#       Q.enqueue(w)
  
  
def iterative_BFS(start_v):
    queue = collections.deque()
    queue.append(start_v)
    discovered = [start_v]
    while queue:
        last = queue.popleft()
        for w in graph[last]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered
  
  # queueBFS(1)

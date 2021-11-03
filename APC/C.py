from collections import deque
import sys

sys.stdin = open("input.txt", "r")

backward = deque([])
frontward = deque([])
access = deque([])
cache = 0

n, q, c = map(int, input().split())
cap = [0]
cap += list(map(int, input().split()))

do = deque([])
for q in range(q):
    do.append(tuple(map(str, input().split())))

# print(do)
# print(cap)

now_page = 0
prev_page = 0
for i in range(q + 1):
    now = do.popleft()
    if now[0] == 'B':
        if len(backward) <= 0:
            continue

        else:
            frontward.append(now_page)
            now_page = backward.pop()

    if now[0] == 'F':
        if len(backward) <= 0:
            continue
        else:
            frontward.append(now_page)

    if now[0] == 'A':
        while frontward:
            delete_page = int(frontward.popleft())
            cache -= cap[delete_page]

        now_page = int(now[1])
        cache += cap[now_page]

        if cache > 20:
            delete_page = int(backward.pop(0))
            cache -= cap[int(delete_page)]

        prev_page = now_page
        if prev_page == 0:
            continue
        else:
            backward.append(prev_page)

    if now[0] == 'C':
        temp = []
        for j in range(1, len(backward)):
            if backward[j] != backward[j - 1]:
                temp.append(backward[j - 1])
        backward = temp

    # print(f'{i + 1}번째 작업 , {now[0]} , backward: {backward}, now_page: {now_page}, frontward:{frontward}, cache:{cache}')

print(now_page)
backward.reverse()
if len(backward) == 0:
    print(-1)
else:
    print(*backward)
if len(frontward) == 0:
    print(-1)
else:
    print(*frontward)

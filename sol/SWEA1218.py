# 괄호 짝 찾기

import sys
sys.stdin = open("input.txt", "r")

import re

for t in range(10):
    length = int(input())
    inp = str(input())
    stack = []
    #left = ['{', '[', '(', '<']
    dic = {'}': '{', ']': '[', ')': '(', '>': '<', '\'': '\''}
    result = 0
    for i in range(length):
        if inp[i] in dic:
            if stack[-1] == dic[inp[i]]:
                stack.pop()
                continue
        stack.append(inp[i])

    if len(stack) == 0:
        result = 1
    print(inp)
    print(stack)

    print(f'#{t+1} {result}')

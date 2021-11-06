def solution(number, k):
    i = 0
    while i < len(number) - 1 and k > 0:
        if number[i] < number[i + 1]:
            number = number[:i] + number[i + 1:]
            # print(number)
            if i != 0:
                i -= 1
            k -= 1
        else:
            i += 1
    if k > 0:
        return number[:-k]
    return number

# 스택활용
def solution2(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
def solution(name):
    answer = 0
    finished = [0 for _ in range(len(name))]
    # alpha = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, X, Y, Z]
    alpha_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 13,
        'M': 14,
        'N': 15,
        'O': 16,
        'P': 17,
        'Q': 18,
        'R': 19,
        'S': 20,
        'T': 21,
        'U': 22,
        'V': 23,
        'W': 24,
        'X': 25,
        'Y': 26,
        'Z': 27,
    }

    ud_count = 0
    lr_count = 0
    # 위아래 count
    for char in name:
        if char != 'A':
            lr_count += min(alpha_dict[char] - 1, 28 - alpha_dict[char])

    A_num = name.count('A')
    # 좌우 count
    ud_count = len(name) - A_num
    count = lr_count + ud_count

    return count

print(solution("JEROEN"))
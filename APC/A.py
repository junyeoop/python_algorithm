import sys

sys.stdin = open("input.txt", "r")

birthday = str(input())
n = int(input())
date_list = []
for i in range(n):
    date_list.append(str(input()))
max_bio = 0
index = 0
for i in range(n):
    bio_y = 0
    for j in range(4):
        bio_y += (int(birthday[j]) - int(date_list[i][j])) ** 2
    bio_m = (int(birthday[4]) - int(date_list[i][4])) ** 2 + (int(birthday[5]) - int(date_list[i][5])) ** 2
    bio_d = (int(birthday[6]) - int(date_list[i][6])) ** 2 + (int(birthday[7]) - int(date_list[i][7])) ** 2
    bio = bio_d * bio_m * bio_y
    if bio > max_bio:
        max_bio = bio
        index = i
    if bio == max_bio:
        if int(date_list[index]) > int(date_list[i]):
            index = i
print(date_list[index])

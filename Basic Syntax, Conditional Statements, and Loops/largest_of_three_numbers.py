flag = True

for _ in range(3):
    num = int(input())
    if flag:
        max_num = num
        flag = False
    if num > max_num:
        max_num = num

print(max_num)

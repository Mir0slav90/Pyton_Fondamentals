flag = True

while flag:
    numb = float(input())
    if 1 <= numb <= 100:
        print(f'The number {numb} is between 1 and 100')
        flag = False

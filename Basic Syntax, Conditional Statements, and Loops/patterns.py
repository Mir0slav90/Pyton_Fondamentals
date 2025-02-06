# testing function pattern
def pattern(start, end, step):
    for i in range(start, end, step):
        print('*' * i)

number = int(input())

pattern(0, number + 1, +1)
pattern(number - 1, 0, -1)

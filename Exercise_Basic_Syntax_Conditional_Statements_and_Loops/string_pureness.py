numb = int(input())
current_string = ''

for _ in range(numb):
    string = input()

    if ',' in string or '.' in string or '_' in string:
        current_string = f'{string} is not pure!'

    else:
        current_string = f'{string} is pure.'

    print(current_string)

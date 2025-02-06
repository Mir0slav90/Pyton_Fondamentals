coffe_count = 0
command = input()

while command != 'END':
    if (command.lower() == 'coding' or
        command.lower() == 'cat' or
        command.lower() == 'dog' or
        command.lower() == 'movie'):
        if command.islower():
            coffe_count += 1
        else:
            if command.isupper():
                coffe_count += 2
    command = input()

if coffe_count > 5:
    print('You need extra sleep')
else:
    print(coffe_count)

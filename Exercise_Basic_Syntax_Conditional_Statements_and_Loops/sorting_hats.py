name = input()
string = ''

while True:
    if name == 'Welcome!':
        print('Welcome to Hogwarts.')
        break
    elif name == 'Voldemort':
        print('You must not speak of that name!')
        break
    elif len(name) > 6:
        string = f'{name} goes to Hufflepuff.'
    elif len(name) == 6:
        string = f'{name} goes to Ravenclaw.'
    elif len(name) == 5:
        string = f'{name} goes to Slytherin.'
    else:
        string = f'{name} goes to Gryffindor.'
    print(string)
    name = input()

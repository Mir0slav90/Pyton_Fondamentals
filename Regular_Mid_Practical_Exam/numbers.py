list_of_numbers = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == "Finish":
        print(*new_list_of_numbers)
        break

    elif command[0] == "Add":
        list_of_numbers.append(int(command[1]))

    elif command[0] == "Remove":
        remove_number = int(command[1])
        if remove_number in list_of_numbers:
            list_of_numbers.remove(remove_number)

    elif command[0] == "Replace":
        number = int(command[1])
        replace_number = int(command[2])

        if number in list_of_numbers:
            idx = list_of_numbers.index(number)
            list_of_numbers[idx] = replace_number

    elif command[0] == "Collapse":
        min_number = int(command[1])
        new_list_of_numbers = list_of_numbers
        for num in list_of_numbers:
            if num < min_number:
                new_list_of_numbers.remove(num)

        list_of_numbers = new_list_of_numbers
        
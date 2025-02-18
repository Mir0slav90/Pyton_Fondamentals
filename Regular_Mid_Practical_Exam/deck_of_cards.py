list_of_cards = list( input().split(', '))
n = int(input())

result = ''
for i in range (n):

    command = input().split(', ')
    if command[0] == "Add":
        if command[1] in list_of_cards:
            result ="Card is already in the deck"
        else:
            list_of_cards.append(command[1])
            result ="Card successfully added"

    elif command[0] == "Remove":
        if  command[1] not in list_of_cards:
            result ="Card not found"
        else:
            list_of_cards.remove(command[1])
            result ="Card successfully removed"

    elif command[0] == "Remove At":
        index_to_remove = int(command[1])
        if 0 <= index_to_remove < len(list_of_cards):
            list_of_cards.pop(index_to_remove)
            result ="Card successfully removed"
        else:
            result ="Index out of range"

    elif command[0] == "Insert":
        index = int(command[1])
        card_name = command[2]
        if 0 <= index < len(list_of_cards):
            if card_name in list_of_cards:
                result ="Card is already added"
            else:
                list_of_cards.insert(index,card_name)
                result ="Card successfully added"
        else:
            result ="Index out of range"
    print(result)

print(", ".join(list_of_cards))

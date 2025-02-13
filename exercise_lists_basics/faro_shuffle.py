string_of_cards = input().split()
count_of_faro_shuffles = int(input())
count = 0

for card in string_of_cards:
    left_half = string_of_cards[ :len(string_of_cards) // 2]
    right_half = string_of_cards[len(string_of_cards) // 2 : ]

while count != count_of_faro_shuffles:
    faro_shuffled_deck = []

    for  i in range(len(left_half)):
        faro_shuffled_deck.append(left_half[i])
        faro_shuffled_deck.append(right_half[i])

    for card in string_of_cards:
        left_half = faro_shuffled_deck[ :len(faro_shuffled_deck) // 2]
        right_half = faro_shuffled_deck[len(faro_shuffled_deck) // 2: ]

    count += 1
print(faro_shuffled_deck)

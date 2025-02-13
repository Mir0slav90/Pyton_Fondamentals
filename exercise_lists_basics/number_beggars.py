string_of_money = input().split(', ')
count_of_beggars = int(input())

money_as_integers = []

for money in string_of_money:
    money_as_integers.append(int(money))

sum_of_beggars = list()
start_index = 0

for _ in range(count_of_beggars):
    current_beggar_money = 0
    for index in range(start_index, len(money_as_integers), count_of_beggars):
        current_beggar_money += money_as_integers[index]

    sum_of_beggars.append(current_beggar_money)
    start_index += 1

print(sum_of_beggars)

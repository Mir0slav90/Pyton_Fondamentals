budget = int(input())
total_price = 0

while True:
    price = input()

    if price == 'End':
        print('You bought everything needed.')
        break
    else:
        total_price += int(price)
        if total_price > budget:
            print('You went in overdraft!')
            break

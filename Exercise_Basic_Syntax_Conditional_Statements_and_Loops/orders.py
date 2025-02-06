price_of_each_order = 0
total_price = 0
number_of_orders = int(input())

for current_order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_need_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_need_per_day < 1 or capsules_need_per_day > 2000:
        continue

    price_of_each_order = price_per_capsule * days * capsules_need_per_day
    total_price += price_of_each_order
    print(f'The price for the coffee is: ${price_of_each_order:.2f}')

print(f'Total: ${total_price:.2f}')

def owner_coast(owner_income: float, owner_expense: float) -> float:
    profit = owner_income - owner_expense
    return profit

number_of_cities = int(input())
total_profit = 0.0

for current_city in range(1,number_of_cities+1,+1):
    city_name = input()
    owner_incomes = float(input())
    owner_expenses = float(input())
    owner_profit = owner_coast(owner_incomes, owner_expenses)

    if current_city % 3 == 0:
        owner_profit -= (owner_expenses * 0.5)
    if current_city % 5 == 0:
        owner_profit -= (owner_incomes * 0.1)

    total_profit += owner_profit

    print(f'In {city_name} Burger Bus earned {owner_profit:.2f} leva.')

print(f'Burger Bus total profit: {total_profit:.2f} leva.')

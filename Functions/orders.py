def calculate_orders(order : str, quantity : int) -> float:
    price = 0.0
    if order == 'coffee':
        price = quantity * 1.50
    elif order == 'coke':
        price = quantity * 1.40
    elif order == 'water':
        price = quantity* 1.00
    elif order == 'snacks':
        price = quantity * 2.00
    return price
def final_price()-> float:
    price = calculate_orders(order= input() , quantity= int(input()))
    return price

print(f'{final_price():.2f}')

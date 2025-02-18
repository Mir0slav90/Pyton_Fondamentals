def calculator(num1 : int , num2 : int, operator : str) -> int:
    result = 0
    if operator == 'add':
        result = num1 + num2
    elif operator == 'subtract':
        result = num1 - num2
    elif operator == 'divide':
        if num2 != 0:
            result = int(num1 / num2)
    elif operator == 'multiply':
        result = num1 * num2
    return result

operation = input()
number_one , number_two = int(input()), int(input())

print(calculator(number_one, number_two, operation))

n = int(input())

numbers = []

for _ in range(n):
    current_number = int(input())
    numbers.append(current_number)

command = input()

filtered_numbers = []

match  command:
    case "even":
        for num in numbers:
            if num % 2 == 0:
                filtered_numbers.append(num)

    case "odd":
        for num in numbers:
            if num % 2 != 0:
                filtered_numbers.append(num)

    case "positive":
        for num in numbers:
            if num >= 0:
                filtered_numbers.append(num)

    case "negative":
        for num in numbers:
            if num < 0:
                filtered_numbers.append(num)

print(filtered_numbers)

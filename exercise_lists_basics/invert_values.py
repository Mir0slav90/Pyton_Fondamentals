list_of_numbers = input().split()

split_numbers = []

for current_number in list_of_numbers:
    number = int(current_number)
    split_numbers.append(-number)

print(split_numbers)

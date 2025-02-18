string_of_numbers = input().split()
rounded_list = []
for number in string_of_numbers:
    rounded_list.append(round(float(number)))
print(rounded_list)

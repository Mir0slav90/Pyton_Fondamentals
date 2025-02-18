string_of_numbers = input().split()

absolute_value_of_numbers = list()
for i in string_of_numbers:
   absolute_value_of_numbers.append(abs(float(i)))

print(absolute_value_of_numbers)

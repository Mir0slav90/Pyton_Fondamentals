divisor = int(input())
boundary = int(input())

for current_index in range(boundary, divisor, -1):
    if current_index % divisor == 0:
        print(current_index)
        break

factor = int(input())
count = int(input())

multiples_list = []

for index in range(1, count + 1):
    i = index * factor
    multiples_list.append(i)

print(multiples_list)

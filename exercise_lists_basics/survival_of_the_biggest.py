list_of_integers = input().split()
n = int(input()) # integers to remove

integers_as_list = []
for number in list_of_integers:
    integers_as_list.append(int(number))

count = 0
while count != n:
    min_element = integers_as_list[0]
    for i in range(len(integers_as_list)):
        if integers_as_list[i] < min_element:
            min_element = integers_as_list[i]

    integers_as_list.remove(min_element)
    count += 1
print(*integers_as_list, sep=", ")

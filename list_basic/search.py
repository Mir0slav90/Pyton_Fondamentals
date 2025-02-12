n = int(input())
word = input()

my_list = []

for _ in range(n):
    current_string = input()
    my_list.append(current_string)

print(my_list)

new_list = []
for i in range(len(my_list)):
    if word in my_list[i]:
        new_list.append(my_list[i])

print(new_list)

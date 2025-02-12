number = int(input())

positives_list = list()
negatives_list = list()

for idx in range(number):
    numb = int(input())
    if numb < 0:
        negatives_list.append(numb)
    else:
        positives_list.append(numb)
print(positives_list)
print(negatives_list)
print(f'Count of positives: {len(positives_list)}\nSum of negatives: {sum(negatives_list)}')

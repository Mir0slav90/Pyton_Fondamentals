year = int(input())

while True:
    year += 1
    year_st = str(year)

    if len(set(year_st)) == len(year_st):
        break

print(year)

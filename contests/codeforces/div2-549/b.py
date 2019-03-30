nr = int(input())


def prod_nr(nr):
    if not nr:
        return 0

    d = 1

    while nr:
        d *= nr % 10
        nr = nr // 10

    return d


def sum_nr(nr):
    d = 0

    while nr:
        d += nr % 10
        nr = nr // 10

    return d


numbers = [nr]
count = 0
nines = 0

while nr:
    nr = nr // 10
    nines = nines * 10 + 9
    count += 1

    if not nr:
        break
    numbers.append((nr - 1) * 10 ** count + nines)


max_nr = 0
_max = 0
for nr in numbers:
    res = prod_nr(nr)
    if res > max_nr:
        max_nr = res
        _max = nr

print(prod_nr(_max))

from collections import OrderedDict


n, m = map(int, input().split())

a = map(int, input().split())
c = map(int, input().split())

dishes = map(list, zip(a, c))
sorted_dishes = sorted(list(zip(range(n), dishes)),
                       key=lambda dish: dish[1][1])
keys = [dish[0] for dish in sorted_dishes]
sorted_dishes = OrderedDict(list(sorted_dishes))
min_dish = 0

while m:
    count = 0
    index, dish = map(int, input().split())

    while dish and min_dish < len(keys):
        if sorted_dishes[index - 1][0] > 0:
            rest = sorted_dishes[index - 1][0] - dish

            if rest > 0:
                count += sorted_dishes[index - 1][1] * dish
                sorted_dishes[index - 1][0] = rest
                break

            count += sorted_dishes[index - 1][0] * sorted_dishes[index - 1][1]
            dish -= sorted_dishes[index - 1][0]
            sorted_dishes[index - 1][0] = 0
        elif index != keys[min_dish] + 1:
            index = keys[min_dish] + 1
        else:
            min_dish += 1
            if min_dish >= len(keys):
                break
            index = keys[min_dish] + 1

    if min_dish >= len(keys):
        print(0)
    else:
        print(count)

    m -= 1

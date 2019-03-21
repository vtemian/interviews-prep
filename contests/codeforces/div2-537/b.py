from decimal import Decimal as D
from statistics import mean


n, k, m = map(int, input().split())

heroes = sorted(map(D, input().split()))[::-1]
max_avg = 0
count = 0
buffed_heroes = []

while m:
    hero = new_hero = heroes[count]
    buff_me = False
    trim_me = False

    if m - k >= 0:
        new_hero = hero + k
    else:
        new_hero = hero + (k - m)

    hero_avg = mean(buffed_heroes + [new_hero] + heroes[count:] or [0.0])
    trim_avg = mean(buffed_heroes + heroes[count:min(count, m)] or [0.0])

    if trim_avg > hero_avg:
        max_avg = trim_avg
        break

    max_avg = hero_avg
    buffed_heroes.append(new_hero)
    m = max(m -k , 0)
    count += 1

print("{0:.10f}".format(max_avg or heroes[0]))

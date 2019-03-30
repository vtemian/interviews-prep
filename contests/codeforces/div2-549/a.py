from collections import Counter

n = int(input())

doors = list(map(int, input().split()))
index = Counter(doors)
counter = 0

if 0 not in index or 1 not in index:
    print(counter)
else:
    for door in doors:
        index[door] -= 1
        counter += 1

        if index[door] == 0:
            print(counter)
            break

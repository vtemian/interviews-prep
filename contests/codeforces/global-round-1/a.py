b, k = map(int, input().split())
a = list(map(int, input().split()))


nr = 0
r_b = b
even = odd = 0
b = b % 10
is_b_even = b % 2 == 0


for idx, aa in enumerate(a):
    aa %= 10

    if idx == len(a) - 1 and aa:
        even += int(aa % 2 == 0)
        odd += int(aa % 2 == 1)
    else:
        if aa % 2 == 0:
            even += 1
        else:
            if is_b_even:
                even += 1
            else:
                odd += 1


if odd % 2 == 0:
    print('even')
else:
    print('odd')

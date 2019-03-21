n = int(input())


def solve():
    no_digits = int(input())
    seq = input()
    if len(seq) < 2:
        print('NO')
        return

    first = seq[0]
    if not int(first) < int(seq[1:]):
        print('NO')
        return

    print('YES')
    print('2')
    print(first, seq[1:])


while n:
    solve()
    n -= 1

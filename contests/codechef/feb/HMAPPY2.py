n = int(input())


def solve():
    n, a, b, k = map(int, input().split())
    output = "Win" if n / a + n / b - (n / (a * b) * 2) < k else "Lose"
    print(output)


while n:
    solve()
    n -= 1

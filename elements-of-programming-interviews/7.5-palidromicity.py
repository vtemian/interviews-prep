def is_palindrom(x: str) -> bool:
    start = 0
    end = len(x) - 1

    while start < end:
        while not x[start].isalpha() and start < end:
            start += 1

        while not x[end].isalpha() and start < end:
            end -= 1

        if x[end].lower() != x[start].lower():
            return False

        start += 1
        end -= 1

    return True


assert is_palindrom("A123 B 123B A")
assert is_palindrom("123 111 1 1 1 1AA 121 12313 123123123")

def compute(number: int)  -> int:
    root = number

    start = 1
    end = number // 2


    while start <= end:
        root = (start + end) // 2

        if root ** 2 > number:
            end = root - 1
        else:
            start = root + 1

    return root


for test, expected in [
    (4, 2),
    (1, 1),
    (0, 0),
    (625, 25),
    (620, 24),
    (8, 3),
]:
    result = compute(test)
    assert result == expected, result

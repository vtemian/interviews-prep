PHONE = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
}


def solve(order: str):
    def partial(index: int):
        if index >= len(order):
            return []

        digit = order[index]
        if digit not in PHONE:
            return partial(index + 1)

        result = []
        for letter in PHONE.get(digit, ''):
            parts = partial(index + 1)
            if not parts:
                result.append(letter)
            else:
                for part in parts:
                    result.append(letter + part)

        return result

    return partial(0)


assert solve('23') == ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
assert solve('123') == ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']

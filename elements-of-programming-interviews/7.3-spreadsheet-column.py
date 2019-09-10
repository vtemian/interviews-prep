def spreadsheet(x: str) -> int:
    result = 0

    for c in x:
        result = result * 26 + ord(c) - ord('A') + 1

    return result


assert spreadsheet('D') == 4
assert spreadsheet('ZZ') == 702
assert spreadsheet('AA') == 27

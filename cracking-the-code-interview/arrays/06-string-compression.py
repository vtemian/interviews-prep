def string_compression(string: str) -> str:
    if not string or len(string) < 2:
        return string

    compressed = ""
    index = 1

    while index < len(string):
        track = 0
        prev_letter = string[index - 1]
        current_letter = string[index]

        while prev_letter == current_letter and index < len(string):
            track += 1
            index += 1

            prev_letter = string[index - 1]
            current_letter = string[index]

        compressed += "{}{}".format(prev_letter, track or 1)
        index += 1
        track = 0

    compressed += "{}{}".format(current_letter, track or 1)

    return compressed if len(compressed) < len(string) else string


for test_case, expected_result in [
        ('', ''),
        ('1', '1'),
        ('aaaab', 'a3b1'),
        ('aaaaaacb', 'a5c1b1'),
        ('asd', 'asd')
]:
    result = string_compression(test_case)
    assert result == expected_result, "{} != {}".format(result, expected_result)

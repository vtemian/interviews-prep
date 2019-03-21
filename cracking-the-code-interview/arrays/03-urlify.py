def urlify_replace(url: str) -> str:
    return url.replace(' ', '%20')


def urlify(url: str) -> str:
    new_url = ''

    for letter in url:
        if letter == ' ':
            new_url += '%20'
        else:
            new_url += letter

    return new_url


for test_case, expected_result in [
    ('1 1', '1%201'),
    ('1     1', '1%20%20%20%20%201'),
    ('', ''),
    (' 1 ', '%201%20'),
]:
    assert urlify_replace(test_case) == expected_result
    assert urlify(test_case) == expected_result

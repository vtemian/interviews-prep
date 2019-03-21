def is_substr(kid: str, parent: str) -> bool:
    return kid in parent


def string_rotation(suspect: str, orig: str) -> bool:
    return is_substr(orig, suspect + suspect)


for test_case, expected_result in [
        (('waterbottle', 'erbottlewat'), True),
        (('1', '2'), False),
]:
    result = string_rotation(*test_case)
    assert result == expected_result, "{} != {}".format(result, expected_result)

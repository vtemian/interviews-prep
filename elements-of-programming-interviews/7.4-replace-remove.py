from typing import List


def solve(string: List[str]) -> List[str]:
    write_idx = idx = aas = bbs = 0

    while idx < len(string):
        letter = string[idx]

        if letter != 'b':
            string[write_idx] = letter
            write_idx += 1

        if letter == 'a':
            aas += 1

        if letter == 'b':
            bbs += 1

        idx += 1

    if aas - bbs > 0:
        for _ in range(aas - bbs):
            string.append('')

    cur_idx = write_idx - 1
    start_idx = len(string) - 1

    while cur_idx >= 0:
        if string[cur_idx] == 'a':
            string[start_idx] = 'd'
            start_idx -= 1
            string[start_idx] = 'd'
            start_idx -= 1
        else:
            string[start_idx] = string[cur_idx]
            start_idx -= 1
        cur_idx -= 1

    return string


print(solve(['a', 'a', 'b', 'c']))

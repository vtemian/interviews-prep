from collections import Counter


s = input()
t = input()


def is_voew(letter):
    return letter in 'aeiou'


def solve(s, t):
    if len(s) != len(t):
        return False

    for index, s_letter in enumerate(s):
        t_letter = t[index]

        if is_voew(s_letter):
            if not is_voew(t_letter):
                return False
        else:
            if is_voew(t_letter):
                return False

    return True


print('No' if not solve(s,t ) else 'Yes')

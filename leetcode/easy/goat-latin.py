class Solution:
    def toGoatLatin(self, S: str) -> str:
        result = []

        for idx, word in enumerate(S.split()):
            word = list(word)
            new_word = word

            if word[0].upper() not in 'AEIOU':
                new_word = word[1:]
                new_word.append(word[0])

            new_word.append('m')
            new_word.append('a')

            new_word.extend(['a'] * (idx + 1))

            result.append(''.join(new_word))

        return ' '.join(result)

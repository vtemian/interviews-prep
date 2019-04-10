class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        NUMBERS = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

        if not s:
            return 0

        number = 0
        count = 0

        while count < len(s):
            first = s[count]
            second = ''

            if count + 1 < len(s):
                second = s[count + 1]

            if first + second in NUMBERS:
                number += NUMBERS[first + second]
                count += 1
            else:
                number += NUMBERS[first]

            count += 1

        return number


result = Solution().romanToInt('MMXXIXIV')
print(result)

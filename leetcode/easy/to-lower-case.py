"""

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.



Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
"""


class Solution:
    def toLowerCase(self, string):
        """
        :type str: str
        :rtype: str
        """

        uppercase_to_lowercase = {
            'Q': 'q',
            'W': 'w',
            'E': 'e',
            'R': 'r',
            'T': 't',
            'Y': 'y',
            'U': 'u',
            'I': 'i',
            'O': 'o',
            'P': 'p',
            'A': 'a',
            'S': 's',
            'D': 'd',
            'F': 'f',
            'G': 'g',
            'H': 'h',
            'J': 'j',
            'K': 'k',
            'L': 'l',
            'Z': 'z',
            'X': 'x',
            'C': 'c',
            'V': 'v',
            'B': 'b',
            'N': 'n',
            'M': 'm'
        }

        return ''.join([
            uppercase_to_lowercase.get(letter, letter)
            for letter in string
        ])


result = Solution().toLowerCase('LOVELY')
print(result)

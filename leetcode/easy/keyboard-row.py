"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of
American keyboard like the image below.

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""


class Solution:
    def findWords(self, words):
        keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

        new_words = []
        for word in words:
            tested_word = word.lower()

            for row in keyboard:
                was_ok = False

                for letter in tested_word:
                    if letter not in row:
                        break
                    was_ok = True
                else:
                    new_words.append(word)
                    checked = True
                    break

                if was_ok:
                    break


        return new_words


result = Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])
print(result)

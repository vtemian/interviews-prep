class Solution:
    def countAndSay(self, n: int) -> str:
        if not n:
            return ""

        result = "1"
        current = 1

        while current < n:

            new_result = ""
            idx = 0

            while idx < len(result):
                letter = result[idx]
                count = 1

                while idx + 1 < len(result) and result[idx + 1] == letter:
                    count += 1
                    idx += 1

                new_result += "{}{}".format(count, letter)

                idx += 1

            result = new_result

            current += 1

        return result


result = Solution().countAndSay(3)
print(result)

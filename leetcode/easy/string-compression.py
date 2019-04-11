class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        idx = 0
        position = 0
        result = 0

        while idx < len(chars):
            letter = chars[idx]
            count = 1

            while idx + 1 < len(chars) and chars[idx + 1] == letter:
                count += 1
                idx += 1

            if count > 1:
                chars[position] = letter
                result += 1
                position += 1

                for tmp_idx, letter in enumerate(str(count)):
                    chars[position] = letter

                    result += 1
                    position += 1

            else:
                chars[position] = letter
                position += 1
                result += 1
            idx += 1

        return result


result = Solution().compress(
["a","b","b","b","b","b","b","b","b","b","b","b","b"])
print(result)

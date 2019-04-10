class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        if len(b) > len(a):
            a, b = b, a

        a = a[::-1]
        b = b[::-1]

        count = 0
        remainder = 0
        result = ""

        while count < len(b):
            b_a = a[count]
            b_b = b[count]

            result += str((int(b_a) + int(b_b) + remainder) % 2)
            remainder = (int(b_a) + int(b_b) + remainder) / 2

            count += 1

        while count < len(a):
            b_a = a[count]

            result += str((int(b_a) + remainder) % 2)
            remainder = (int(b_a) + remainder) / 2

            count += 1

        if remainder:
            result += str(remainder)

        return result[::-1]


result = Solution().addBinary('1010', '1011')
print(result)

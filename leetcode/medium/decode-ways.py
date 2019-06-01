class Solution:
    def numDecodings(self, s: str) -> int:
        def is_letter(idx):
            c1 = s[idx - 1]
            c2 = s[idx]

            if c1 == "1":
                return c2 >= "0" and c2 <= "9"
            elif c1 == "2":
                return c2 >= "0" and c2 <= "6"
            return False

        if not s:
            return 0

        if len(s) == 1:
            if s[0] == "0":
                return 0
            return 1

        buffer = []

        if s[0] == "0":
            return 0
        buffer.append(1)

        if s[1] == "0":
            if not is_letter(1):
                return 0
            buffer.append(1)
        elif is_letter(1):
            buffer.append(2)
        else:
            buffer.append(1)

        for i in range(2, len(s)):
            if s[i] == "0":
                if is_letter(i):
                    buffer.append(buffer[-2])
                    continue
                return 0

            if is_letter(i):
                buffer.append(buffer[-1] + buffer[-2])
            else:
                buffer.append(buffer[-1])

        return buffer[-1]

class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return s

        stack = []
        idx = 0

        while idx < len(s):
            if s[idx].isdigit():
                nr = []

                while idx < len(s) and s[idx].isdigit():
                    nr.append(s[idx])
                    idx += 1

                stack.append(int("".join(nr)))
                idx -= 1

            if s[idx] == "[":
                stack.append("[")

            if s[idx] == "]":
                string = stack.pop()

                while stack[-1] != "[":
                    string = stack.pop() + string

                stack.pop()
                stack.append(string * stack.pop())

            if s[idx].isalpha():
                string = []

                while idx < len(s) and s[idx].isalpha():
                    string.append(s[idx])
                    idx += 1

                stack.append("".join(string))
                idx -= 1

            idx += 1

        return "".join(stack)

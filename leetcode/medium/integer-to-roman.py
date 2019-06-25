class Solution:
    def intToRoman(self, num: int) -> str:
        idx = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        result = []

        for arab, roman in idx:
            if num // arab > 0:
                result.append(roman * (num // arab))
                num = num % arab

        return "".join(result)

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_no_starting_ones(nr: int) -> int:
            order = 7
            mask = 1 << order
            ones = 0

            while order and mask & nr:
                nr = nr & (mask - 1)
                ones += 1
                order -= 1
                mask = 1 << order

            return ones

        expecting = 0
        for nr in data:
            no_ones = get_no_starting_ones(nr)


            if no_ones == 1 and expecting > 0:
                expecting -= 1
                continue

            if no_ones == 1 and expecting == 0:
                return False

            if no_ones == 0:
                if expecting == 0:
                    continue

                return False

            if expecting == 0:
                if no_ones > 4:
                    return False

                expecting = no_ones - 1
                continue

            return False

        return expecting == 0

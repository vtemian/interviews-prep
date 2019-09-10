from typing import List


def hanoi(n: int):
    rods = [[i for i in range(n, 0, -1)], [], []]

    def _hanoi(moves: int, from_rod: int, to_rod: int, aux_rod: int):
        if not moves:
            return

        _hanoi(moves - 1, from_rod, aux_rod, to_rod)

        print(from_rod, rods[from_rod])

        rods[to_rod].append(rods[from_rod][-1])
        rods[from_rod].pop()

        print(f"Moving {from_rod} to {to_rod}")

        _hanoi(moves - 1, aux_rod, to_rod, from_rod)

    _hanoi(n, 0, 1, 2)


hanoi(4)

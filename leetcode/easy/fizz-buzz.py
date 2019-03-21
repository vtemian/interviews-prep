class Solution:
    def fizzBuzz(self, n: 'int') -> 'List[str]':
        store = []

        for buzzer in range(1, n + 1):
            result = ""

            if buzzer % 3 == 0:
                result += "Fizz"

            if buzzer % 5 == 0:
                result += "Buzz"

            store.append(result or str(buzzer))

        return store

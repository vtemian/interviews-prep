class Solution:
    def is_digit_log(self, log) -> bool:
        for entry in log:
            if not entry.isdigit():
                return False

        return True

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            id, *data = log.split()

            if self.is_digit_log(data):
                log = [id]
                log.extend(data)
                digit_logs.append(log)
            else:
                log = data
                log.extend([id])
                letter_logs.append(log)

        letter_logs = [" ".join([log[-1]] + log[:-1]) for log in sorted(letter_logs)]
        digit_logs = [" ".join(log) for log in digit_logs]

        return letter_logs + digit_logs

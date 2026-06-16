class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calculate_waviness(n):
            if n < 100:
                return 0
            waviness = 0
            digits = [int(d) for d in str(n)]
            for i in range(1, len(digits) - 1):
                if digits[i] > digits[i - 1] and digits[i] > digits[i + 1]:
                    waviness += 1
                elif digits[i] < digits[i - 1] and digits[i] < digits[i + 1]:
                    waviness += 1
            return waviness

        total = 0
        for num in range(num1, num2 + 1):
            total += calculate_waviness(num)
        return total
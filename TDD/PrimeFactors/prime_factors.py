class PrimeFactors:
    def of(self, number) -> []:
        factors = []
        divisor = 2
        while number > 1:
            while number % divisor == 0:
                factors.append(divisor)
                number //= divisor
            divisor += 1

        return factors


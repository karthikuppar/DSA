class karthik:
    def divisor(self, n):
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
        return divisors
    
k = karthik()
print(k.divisor(6))
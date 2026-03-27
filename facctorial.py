class solution:
    def factorial(self,n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)
a=solution()
print(a.factorial(5))
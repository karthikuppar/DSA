class karthik:
    def fib(self,n):
        if n<=1:
            return(n)
        else:
         a=self.fib(n-1)+self.fib(n-2)
         return(a)
b=karthik()
print(b.fib(4))
            
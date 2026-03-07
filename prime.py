class karthik:
    def prime(self,n):
         if n<=1:
            return False
         for i in range(2,n):#if not we can write for i in range(2,int(n**0.5)+1) to reduce the time complexity
            if n%i==0:
             return False
         return True
a=karthik()
print(a.prime(37))
            
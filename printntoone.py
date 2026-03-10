class Solution:
    def printNumbers(self, n):
        print(n)
        if(n==1):
            print
        else: 
            return(self.printNumbers(n-1))    
a=Solution()
(a.printNumbers(5))
class Solution:
    def countDigit(self, n):
        if n==0:
            return 1
        
        cnt=0
        while n > 0:
            cnt+=1
            n=n//10
        return(cnt) 
a=Solution()
print(a.countDigit (123400))
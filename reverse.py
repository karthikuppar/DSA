class Solution:
    def reverseNumber(self, n):
        revNum = 0
        while n > 0:
            lastDigit = n % 10
            revNum = revNum * 10 + lastDigit
            n = n // 10
        return revNum
obj = Solution()
num = 12345
print(obj.reverseNumber(num))  

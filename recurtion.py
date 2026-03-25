class Solution:
    def sumOfNaturalNumbers(self, N):
        if N == 1:
            return 1
        return N + self.sumOfNaturalNumbers(N - 1)

obj = Solution()
print(obj.sumOfNaturalNumbers(4))

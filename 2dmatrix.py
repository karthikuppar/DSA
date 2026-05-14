class Solution:
    def searchMatrix(self, mat, target):
        m = len(mat)
        n = len(mat[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            # Convert 1D index → 2D index
            row = mid // n
            col = mid % n

            if mat[row][col] == target:
                return True
            elif mat[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
a = Solution()
mat = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3  
print(a.searchMatrix(mat, target))
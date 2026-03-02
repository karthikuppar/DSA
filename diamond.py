class Solution:
    # Function to print Pattern 7
    def pattern7(self, N):
        # Outer loop for rows
        for i in range(N):

            # Print leading spaces
            for j in range(N - i - 1):
                print(" ", end="")

            # Print stars
            for j in range(2 * i + 1):
                print("*", end="")

            # Move to next row
            print()

    # Function to print reverse pyramid
    def pattern8(self, N):
        # Outer loop for rows
        for i in range(N):
            # Print leading spaces
            for j in range(i):
                print(" ", end="")
            # Print stars
            for j in range(2 * N - (2 * i + 1)):
                print("*", end="")
            # Move to next row
            print()

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern7(N)
    sol.pattern8(N)
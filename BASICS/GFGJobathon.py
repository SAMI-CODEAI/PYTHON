class Solution:
    def totalCount(self, n: int) -> int:
        # Compute sum(n) efficiently
        total_sum = n * (n + 1) // 2

        # Compute xor(0 to n)
        xor_n = [n, 1, n + 1, 0][n % 4]  # Optimized pattern for XOR from 0 to n

        # If sum(n) and xor_n are equal, sum all numbers from 0 to n
        if total_sum == xor_n:
            return sum(range(n + 1))
        else:
            return 0  # No valid x found

# Driver Code
def main():
    tt = int(input())  # Read number of test cases
    for _ in range(tt):
        n = int(input())  # Read n
        ob = Solution()
        print(ob.totalCount(n))
        print("~")

if __name__ == "__main__":
    main()

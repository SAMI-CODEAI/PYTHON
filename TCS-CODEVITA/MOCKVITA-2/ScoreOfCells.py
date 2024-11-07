def find_cells_with_score_k(n, m, table, k):
    # Initialize dp table to count ways to each cell
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1  # Start point

    # Populate dp table
    for i in range(n):
        for j in range(m):
            # Move right
            if j + 1 < m and table[i][j + 1] >= table[i][j]:
                dp[i][j + 1] += dp[i][j]
            # Move down
            if i + 1 < n and table[i + 1][j] >= table[i][j]:
                dp[i + 1][j] += dp[i][j]

    # Collect cells with score k
    result = []
    for i in range(n):
        for j in range(m):
            if dp[i][j] == k:
                result.append((i, j))

    # Output results
    if result:
        for cell in result:
            print(cell[0], cell[1])
    else:
        print("NO")

# Input handling
def main():
    n, m = map(int, input().strip().split())
    table = [list(map(int, input().strip().split())) for _ in range(n)]
    k = int(input().strip())
    find_cells_with_score_k(n, m, table, k)

if __name__ == "__main__":
    main()

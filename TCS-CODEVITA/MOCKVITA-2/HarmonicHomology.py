def max_concordance_score(hierarchy, melody1, melody2, A, B, C):
    # Create tune hierarchy mappings
    tune_parent = {}
    level_dict = {}

    # Build the parent and level structure
    def build_hierarchy(parent, children, level):
        for child in children:
            tune_parent[child] = parent
            level_dict[child] = level

    # Parse hierarchy data
    for parent, children in hierarchy.items():
        level = level_dict.get(parent, 0) + 1
        build_hierarchy(parent, children, level)

    def are_similar(tune1, tune2):
        # Tunes are similar if they are the same or belong to the same level
        return tune1 == tune2 or level_dict.get(tune1, -1) == level_dict.get(tune2, -1)

    # DP setup
    len1, len2 = len(melody1), len(melody2)
    dp = [[float('-inf')] * (len2 + 1) for _ in range(len1 + 1)]
    dp[0][0] = 0

    # Fill DP table
    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i > 0:
                # Remove from melody1
                dp[i][j] = max(dp[i][j], dp[i - 1][j] - C)
            if j > 0:
                # Remove from melody2
                dp[i][j] = max(dp[i][j], dp[i][j - 1] - C)
            if i > 0 and j > 0:
                # Compare tunes
                if are_similar(melody1[i - 1], melody2[j - 1]):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + A)
                else:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] - B)

    return dp[len1][len2]


# Input processing
def main():
    # Number of parent nodes
    n = int(input().strip())
    hierarchy = {}
    for _ in range(n):
        line = input().strip().split(" : ")
        parent = line[0].strip()
        children = line[1].strip().split()
        hierarchy[parent] = children

    # Parse melodies
    melody1 = input().strip().split("-")
    melody2 = input().strip().split("-")

    # Parse A, B, C values
    A, B, C = map(int, input().strip().split())

    # Calculate maximum concordance score
    result = max_concordance_score(hierarchy, melody1, melody2, A, B, C)
    print(result)


if __name__ == "__main__":
    main()

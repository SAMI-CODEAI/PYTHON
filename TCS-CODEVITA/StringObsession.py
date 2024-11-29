def max_substrings_removed(main_string, substrings):
    # Use a dictionary to memoize results for already processed strings
    memo = {}

    # Recursive function to find maximum substrings we can remove
    def helper(s):
        # If this string has been processed before, return the result from memo
        if s in memo:
            return memo[s]

        # Initialize the max count as 0 (if no removal is possible)
        max_count = 0

        # Try to remove each substring from the current string
        for sub in substrings:
            if sub in s:
                # Remove the first occurrence of sub and call helper on the new string
                new_string = s.replace(sub, '', 1)
                max_count = max(max_count, 1 + helper(new_string))

        # Store the result in the memo dictionary and return it
        memo[s] = max_count
        return max_count

    # Start the recursive process with the original main string
    return helper(main_string)


# Input reading
n = int(input())  # Number of substrings
substrings = input().split()  # List of substrings
main_string = input()  # The main string

# Calculate and output the result
result = max_substrings_removed(main_string, substrings)
print(result)

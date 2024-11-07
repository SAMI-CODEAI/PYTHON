def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))


def process_string(binary_string, A, B):
    # Count the number of '0's and '1's
    count_0 = binary_string.count('0')
    count_1 = binary_string.count('1')

    # Calculate cost for possible rearrangements
    cost1 = min(A, B) * (min(count_0, count_1))

    # Create the string that minimizes the cost
    if A < B:
        rearranged = '0' * count_0 + '1' * count_1
    else:
        rearranged = '1' * count_1 + '0' * count_0

    # Calculate the hamming distance
    hamming_dist = hamming_distance(binary_string, rearranged)

    return hamming_dist


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    T = int(data[0].strip())
    result = []

    index = 1
    for _ in range(T):
        binary_string = data[index].strip()
        index += 1
        A, B = map(int, data[index].strip().split())
        index += 1

        # Validate if binary_string contains only 0s and 1s
        if not all(c in '01' for c in binary_string):
            result.append("INVALID")
        else:
            result.append(process_string(binary_string, A, B))

    for res in result:
        print(res)


if __name__ == "__main__":
    main()

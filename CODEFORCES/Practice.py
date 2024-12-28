def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    idx = 0
    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx].split()))
        idx += 1

        moves = []

        # Start processing the columns
        for i in range(n - 1):
            # If the current column has more inscriptions than the next one
            while a[i] > a[i + 1]:
                # Move an inscription from a[i] to a[i+1]
                a[i] -= 1
                a[i + 1] += 1
                moves.append((i + 1, i + 2))  # 1-based indexing

        results.append(f"{len(moves)}")
        for move in moves:
            results.append(f"{move[0]} {move[1]}")

    sys.stdout.write("\n".join(results) + "\n")


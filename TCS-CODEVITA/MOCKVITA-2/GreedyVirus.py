from collections import deque


def get_neighbors(x, y, m, n):
    # Returns the list of valid neighboring positions (within bounds)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            neighbors.append((nx, ny))
    return neighbors


def min_fudge_to_reach_dummy(m, n, grid, virus_pos, dummy_pos):
    start_x, start_y = virus_pos
    target_x, target_y = dummy_pos

    # BFS queue with (x, y, fudged_data_sum)
    queue = deque([(start_x, start_y, 0)])
    # Store minimum fudge required to reach each cell
    min_fudge = [[float('inf')] * n for _ in range(m)]
    min_fudge[start_x][start_y] = 0

    while queue:
        x, y, fudged_data = queue.popleft()

        # Check if we've reached the target
        if (x, y) == (target_x, target_y):
            return fudged_data

        # Explore all neighbors
        neighbors = get_neighbors(x, y, m, n)
        max_data_in_neighborhood = max(grid[nx][ny] for nx, ny in neighbors)

        # Try to move to each neighbor by adding the minimum fudge necessary
        for nx, ny in neighbors:
            if grid[nx][ny] < max_data_in_neighborhood:
                # Fudge required to make (nx, ny) the highest in neighborhood
                required_fudge = max_data_in_neighborhood - grid[nx][ny] + 1
            else:
                required_fudge = 0

            total_fudged_data = fudged_data + required_fudge

            # If this is the minimum fudge required to reach (nx, ny), continue BFS
            if total_fudged_data < min_fudge[nx][ny]:
                min_fudge[nx][ny] = total_fudged_data
                queue.append((nx, ny, total_fudged_data))

    # If no path to dummy container, return -1 (should not happen as per problem)
    return -1


# Input processing
def main():
    m, n = map(int, input().strip().split())
    grid = [list(map(int, input().strip().split())) for _ in range(m)]
    virus_pos = tuple(map(lambda x: int(x) - 1, input().strip().split()))  # Adjusting for 1-based index
    dummy_pos = tuple(map(lambda x: int(x) - 1, input().strip().split()))  # Adjusting for 1-based index

    result = min_fudge_to_reach_dummy(m, n, grid, virus_pos, dummy_pos)
    print(result)


if __name__ == "__main__":
    main()

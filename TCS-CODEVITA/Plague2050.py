from collections import deque


# Function to check if a position is valid in the grid
def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


# Function to spread the infection for the next day
def spread_infection(grid, n):
    new_grid = [row[:] for row in grid]  # Create a copy for the next day's state
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '0':  # Check only uninfected cities
                infected_neighbors = 0
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if is_valid(nx, ny, n) and grid[nx][ny] == '1':
                        infected_neighbors += 1
                if infected_neighbors >= 3:
                    new_grid[i][j] = '1'  # City becomes infected
    return new_grid


# BFS function to find the shortest path from the start to the destination
def bfs(grid, start, end, n):
    queue = deque([start])
    visited = set([start])
    distance = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if (x, y) == end:
                return distance
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, n) and (nx, ny) not in visited and grid[nx][
                    ny] != '1':  # Can't move to infected city
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        distance += 1
    return float('inf')


# Main function to simulate the plague spread and compute the minimum days to reach the herb city
def find_days_to_reach_herb(grid, start, end, n):
    days = 0
    while True:
        # Run BFS to check if the destination is reachable on the current day
        path_length = bfs(grid, start, end, n)
        if path_length != float('inf'):
            return days + path_length
        grid = spread_infection(grid, n)  # Update the grid for the next day
        days += 1


# Main function to take input and process the problem
def main():
    # Taking user input for grid size
    n = int(input("Enter the size of the grid (N): ").strip())
    grid = []

    # Taking user input for grid configuration
    print("Enter the grid row by row (values can be 's', 'd', '0', or '1'):")
    for _ in range(n):
        row = input().strip()
        grid.append(list(row))

    # Find the start and destination positions
    start = None
    end = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 's':
                start = (i, j)
            elif grid[i][j] == 'd':
                end = (i, j)

    # Calculate the minimum days required to reach the herb city
    days = find_days_to_reach_herb(grid, start, end, n)
    print(f"Minimum number of days required: {days}")


if __name__ == "__main__":
    main()

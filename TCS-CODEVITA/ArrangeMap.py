from collections import deque
import itertools

# Function to find the shortest path in the grid using BFS
def gsp(placement, N):
    start = None
    end = None
    for i in range(N):
        for j in range(N):
            if placement[i][j] == 'S':
                start = (i, j)
            elif placement[i][j] == 'D':
                end = (i, j)

    if not start or not end:
        return float('inf')  # Return a large number if start or end is not found

    # BFS Setup
    queue = deque([(start, 0)])  # (position, distance)
    visited = {start}

    while queue:
        (x, y), dist = queue.popleft()

        # If we reached destination, return the distance
        if placement[x][y] == 'D':
            return dist

        # Move in all 4 possible directions (up, down, left, right)
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited and placement[nx][ny] != 'L':
                visited.add((nx, ny))
                queue.append(((nx, ny), dist + 1))

    return float('inf')  # Return inf if no path exists

# Function to get individual sheets from the grid
def getSh(placement, N, M):
    sheets = []
    for i in range(0, N, M):
        for j in range(0, N, M):
            sheet = []
            for x in range(M):
                row = []
                for y in range(M):
                    row.append(placement[i + x][j + y])
                sheet.append(row)
            sheets.append(sheet)
    return sheets

# Function to arrange the grid from the sheets
def makeGr(arrangement, sheets, N, M):
    grid = [["" for _ in range(N)] for _ in range(N)]
    num_sheets = N // M

    for idx, sidx in enumerate(arrangement):
        sheet = sheets[sidx]
        bi = (idx // num_sheets) * M
        bj = (idx % num_sheets) * M

        for i in range(M):
            for j in range(M):
                grid[bi + i][bj + j] = sheet[i][j]

    return grid

# Function to solve the problem
def solve():
    N, M = map(int, input().split())
    original_grid = [list(input().strip()) for _ in range(N)]

    # Extract sheets from the original grid
    sheets = getSh(original_grid, N, M)
    num_sheets = (N // M) ** 2

    start_sheet = end_sheet = None
    for i, sheet in enumerate(sheets):
        for row in sheet:
            if 'S' in row:
                start_sheet = i
            if 'D' in row:
                end_sheet = i

    # Initialize the minimum distance as infinity
    min_dist = float('inf')

    # Try permutations of intermediate sheets
    sheet_indices = list(range(num_sheets))
    sheet_indices.remove(start_sheet)
    sheet_indices.remove(end_sheet)

    # Try promising sheet arrangements first (e.g., sheets closer to 'S' or 'D')
    for perm in itertools.permutations(sheet_indices):
        arrangement = [start_sheet] + list(perm) + [end_sheet]
        grid = makeGr(arrangement, sheets, N, M)
        min_dist = min(min_dist, gsp(grid, N))

    return min_dist

# Main entry point
if __name__ == "__main__":
    print(solve())

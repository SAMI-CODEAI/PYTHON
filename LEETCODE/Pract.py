from collections import deque
import itertools

# Function to find the shortest path
def gsp(placementlelo, N):
    start = None
    end = None
    for i in range(N):
        for j in range(N):
            if placementlelo[i][j] == 'S':
                start = (i, j)
            elif placementlelo[i][j] == 'D':
                end = (i, j)

    if not start or not end:
        return float('inf')  # Return a large number if start or end is not found

    queue = deque([(start, 0)])  # BFS setup
    visited = {start}

    while queue:
        (x, y), dist = queue.popleft()
        if placementlelo[x][y] == 'D':
            return dist

        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited and placementlelo[nx][ny] != 'L':
                visited.add((nx, ny))
                queue.append(((nx, ny), dist + 1))

    return float('inf')  # If no path is found, return an infinite distance

# Function to get individual sheets
def getSh(placementlelo, N, M):
    shts = []
    for i in range(0, N, M):
        for j in range(0, N, M):
            sheet = []
            for x in range(M):
                row = []
                for y in range(M):
                    row.append(placementlelo[i + x][j + y])
                sheet.append(row)
            shts.append(sheet)
    return shts

# Function to arrange the grid from the sheets
def makeGr(arrNT, shts, N, M):
    placementlelo = [["" for _ in range(N)] for _ in range(N)]
    numSht = N // M

    for idx, sidx in enumerate(arrNT):
        sheet = shts[sidx]
        bi = (idx // numSht) * M
        bj = (idx % numSht) * M

        for i in range(M):
            for j in range(M):
                placementlelo[bi + i][bj + j] = sheet[i][j]

    return placementlelo

# Main function to solve the problem
def solve():
    N, M = map(int, input().split())
    orgGrid = []
    for _ in range(N):
        orgGrid.append(list(input().strip()))

    # Extract sheets from the grid
    shts = getSh(orgGrid, N, M)
    numSht = (N // M) ** 2

    sst = dst = None
    for i, sheet in enumerate(shts):
        for row in sheet:
            if 'S' in row:
                sst = i
            if 'D' in row:
                dst = i

    min_dist = float('inf')
    nums = list(range(numSht))
    nums.remove(sst)
    nums.remove(dst)

    # Try all permutations of the other sheets
    for midPerm in itertools.permutations(nums):
        arrNT = [sst] + list(midPerm) + [dst]
        placementlelo = makeGr(arrNT, shts, N, M)
        min_dist = min(min_dist, gsp(placementlelo, N))

    return min_dist

if __name__ == "__main__":
    print(solve())

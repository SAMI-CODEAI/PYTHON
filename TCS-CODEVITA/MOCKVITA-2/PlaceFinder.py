import math
import heapq


def parse_input():
    # Number of devices
    n = int(input().strip())

    # Device connections info
    devices_info = input().strip().split()
    device_connections = {}

    # Parse each device's reachable devices count
    for info in devices_info:
        device_id, count = map(int, info.split(':'))
        device_connections[device_id] = count

    # Parse connections between devices with distance and angle
    adjacency_list = {}
    for _ in range(n):
        device_id = int(input().strip())
        adjacency_list[device_id] = []

        for __ in range(device_connections[device_id]):
            connected_device, distance, angle = map(int, input().strip().split())
            # Convert distance and angle to x and y coordinates
            angle_radians = math.radians(angle)
            x = distance * math.cos(angle_radians)
            y = distance * math.sin(angle_radians)
            adjacency_list[device_id].append((connected_device, distance, x, y))

    # Devices between which distance needs to be calculated
    device_a, device_b = map(int, input().strip().split())

    return n, adjacency_list, device_a, device_b


def dijkstra(adjacency_list, start, end):
    # Priority queue for Dijkstra's algorithm
    heap = [(0, start)]
    distances = {node: float('inf') for node in adjacency_list}
    distances[start] = 0

    while heap:
        current_distance, current_device = heapq.heappop(heap)

        if current_device == end:
            return current_distance

        if current_distance > distances[current_device]:
            continue

        for neighbor, distance, _, _ in adjacency_list[current_device]:
            new_distance = current_distance + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    return float('inf')  # If there is no path between start and end


def main():
    n, adjacency_list, device_a, device_b = parse_input()
    distance = dijkstra(adjacency_list, device_a, device_b)
    print(f"{distance:.2f}")


if __name__ == "__main__":
    main()

import math

def is_rectangle(vertices):
    """
    Check if the given vertices form a rectangle.
    :param vertices: List of tuples representing wall vertices.
    :return: True if the shape is a rectangle, False otherwise.
    """
    if len(vertices) != 4:
        return False

    # Extract x and y coordinates
    x_coords = sorted([x for x, y in vertices])
    y_coords = sorted([y for x, y in vertices])

    # A rectangle will have exactly two unique x-coordinates and two unique y-coordinates
    return len(set(x_coords)) == 2 and len(set(y_coords)) == 2

def shoelace_formula(vertices):
    """Calculate the area of a polygon using the shoelace formula."""
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2

def bounding_box_presses(vertices, brush_size):
    """
    Calculate the minimum number of presses using the bounding box approach.
    :param vertices: List of tuples representing wall vertices.
    :param brush_size: Size of the square brush (MxM).
    :return: Minimum number of presses.
    """
    # Find the bounding box of the wall
    min_x = min(x for x, y in vertices)
    max_x = max(x for x, y in vertices)
    min_y = min(y for x, y in vertices)
    max_y = max(y for x, y in vertices)

    # Calculate the dimensions of the bounding box
    width = max_x - min_x
    height = max_y - min_y

    # Calculate the number of presses needed along width and height
    presses_width = math.ceil(width / brush_size)
    presses_height = math.ceil(height / brush_size)

    # Total number of presses is the product of presses along both dimensions
    return presses_width * presses_height

def minimum_presses(vertices, brush_size):
    """
    Determine the minimum number of presses using either shoelace formula or bounding box approach.
    :param vertices: List of tuples representing wall vertices.
    :param brush_size: Size of the square brush (MxM).
    :return: Minimum number of presses.
    """
    if is_rectangle(vertices):
        return bounding_box_presses(vertices, brush_size)
    else:
        # Calculate the area using the shoelace formula
        wall_area = shoelace_formula(vertices)
        brush_area = brush_size * brush_size
        return math.ceil(wall_area / brush_area)

def main():
    # Input and Output
    n = int(input())
    vertices = [tuple(map(int, input().split())) for _ in range(n)]
    brush_size = int(input())

    # Output the result
    print(minimum_presses(vertices, brush_size))

# Example usage
if __name__ == "__main__":
    main()

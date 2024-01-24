import math

def closest_pair_drones(points):
    # Sort points based on x-coordinate
    points.sort(key=lambda point: point[0])

    # Recursive function to find the closest pair
    def closest_pair_recursive(points):
        n = len(points)

        # Base case: If there are only two or three points, compute the distance exhaustively
        if n <= 3:
            return brute_force_closest_pair(points)

        # Divide the points into left and right halves
        mid = n // 2
        left_half = points[:mid]
        right_half = points[mid:]

        # Recursively find the closest pair in each half
        left_closest_pair = closest_pair_recursive(left_half)
        right_closest_pair = closest_pair_recursive(right_half)

        # Determine the minimum distance among the closest pairs in the left and right halves
        min_distance = min(left_closest_pair[0], right_closest_pair[0])
        min_pair = left_closest_pair[1] if left_closest_pair[0] <= right_closest_pair[0] else right_closest_pair[1]

        # Check for pairs that span the dividing line
        strip = [point for point in points if abs(point[0] - points[mid][0]) < min_distance]
        strip.sort(key=lambda point: point[1])

        # Check if there is closer points
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 8, len(strip))):
                distance = euclidean_distance(strip[i], strip[j])
                if distance < min_distance:
                    min_distance = distance
                    min_pair = (strip[i], strip[j])

        return min_distance, min_pair

    # Helper function for brute force computation of closest pair
    def brute_force_closest_pair(points):
        min_distance = float('inf')
        min_pair = None

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = euclidean_distance(points[i], points[j])
                if distance < min_distance:
                    min_distance = distance
                    min_pair = (points[i], points[j])

        return min_distance, min_pair

    return closest_pair_recursive(points)


def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# Example usage:
drones_coordinates = [(1, 2), (4, 6), (7, 8), (9, 5), (3, 1), (10, 3), (2, 12), (5, 11)]
#drones_coordinates = [(1, 2), (1, 6), (1, 8), (1, 50), (1, 10), (1, 3)]

min_distance, min_pair = closest_pair_drones(drones_coordinates)

print(f"Minimum distance: {min_distance}")
print(f"Closest pair: {min_pair}")

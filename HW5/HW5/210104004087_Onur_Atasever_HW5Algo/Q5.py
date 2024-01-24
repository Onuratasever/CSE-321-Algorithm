def max_activated_antennas(antennas):
    # Sort antennas based on ending points in ascending order
    antennas.sort(key=lambda x: x[1])
    print(antennas)
    ending_point = 0
    activated_antennas = []

    for antenna in antennas:
        start_point, end_point = antenna
        #print("ending point: ", ending_point,  "start point: ", start_point, " end point: ", end_point)
        # If the current antenna covers the starting point of the street
        # and is not intersecting with any previously activated antennas
        if start_point >= ending_point and end_point > ending_point:
            # Activate antenna
            activated_antennas.append(antenna)
            # Update ending point to antenna's ending point
            ending_point = end_point
    
    return activated_antennas

# antennas = [(1, 5), (2, 7), (4, 8), (6, 12)]
antennas = [(1, 5), (2, 4), (3, 7), (6, 8), (8, 10), (9, 11), (12, 14), (13, 15)]
result = max_activated_antennas(antennas)
print("activated antennas:", result)

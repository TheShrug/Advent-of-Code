import numpy as numpy
# its fun to visualize this
numpy.set_printoptions(threshold=numpy.inf, linewidth=10000)

coordinates_raw = open("input.txt")
coordinates_list = []
max_coordinates = [0, 0]
infinite_indexes = set()
for line in coordinates_raw:
    coordinates = line.strip("\n").replace(',', '').split(' ')
    coordinates_list.append([int(coordinates[0]), int(coordinates[1])])
    if int(coordinates[0]) > max_coordinates[0]:
        max_coordinates[0] = int(coordinates[0])
    if int(coordinates[1]) > max_coordinates[1]:
        max_coordinates[1] = int(coordinates[1])

grid = numpy.zeros((max_coordinates[0] + 1, max_coordinates[1] + 1), numpy.int16)

for index, coordinate in enumerate(coordinates_list):
    grid[coordinate[0],coordinate[1]] = index + 1

for x_index, x in enumerate(grid):
    for y_index, y in enumerate(grid):
        closest_distance = 9999
        closest_index = 0
        matches_found_at_coord = 0
        distances = []
        for index, coordinate in enumerate(coordinates_list):
            distance = abs(x_index - coordinate[0]) + abs(y_index - coordinate[1])
            distances.append(distance)
            if distance < closest_distance:
                closest_distance = distance
        if distances.count(closest_distance) == 1:
            grid[x_index, y_index] = distances.index(closest_distance) + 1
        if x_index == max_coordinates[0] or x_index == 0 or y_index == max_coordinates[1] or y_index == 0:
            infinite_indexes.add(grid[x_index, y_index])

print(grid)

unique, counts = numpy.unique(grid, return_counts=True)
unique_indexes_in_grid = dict(zip(unique, counts))

for infinite_index in infinite_indexes:
    del unique_indexes_in_grid[infinite_index]

print("max area:", max(unique_indexes_in_grid.values()))

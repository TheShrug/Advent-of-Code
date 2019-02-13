import numpy

numpy.set_printoptions(threshold=numpy.inf, linewidth=10000)


def get_nth_digit(number, n):
    return number // 10**n % 10


def group_total(grid, x, y):
    group_sum = 0
    for i in range(3):
        for j in range(3):
            group_sum += grid[(i + y - 1), (j + x - 1)]
    return group_sum


def set_power_levels(grid, serial_number):
    for yindex, y in enumerate(grid):
        for xindex, value in enumerate(y):
            rack_id = xindex + 1 + 10;
            power_level = rack_id * (yindex + 1)
            power_level = power_level + serial_number
            power_level = power_level * rack_id
            power_level = get_nth_digit(power_level, 2) - 5
            grid[yindex, xindex] = power_level
    return grid


def get_max_group_position(grid, grid_size):
    position_totals = []

    for yindex in range(grid_size - 3):
        for xindex in range(grid_size - 3):
            position_totals.append(((xindex + 1, yindex + 1), group_total(grid, xindex + 1, yindex + 1)))

    max_coord = ()
    max_total = 0

    for position in position_totals:
        if position[1] > max_total:
            max_total = position[1]
            max_coord = position[0]

    return max_coord


input = 9445
grid = numpy.zeros((300,300), numpy.int16)
grid = set_power_levels(grid, input)

print('part 1', get_max_group_position(grid, 300))


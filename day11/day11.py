import numpy

numpy.set_printoptions(threshold=numpy.inf, linewidth=10000000)

"""
I should get better about not shadowing names from outer scope...
"""


def get_nth_digit(number, n):
    return number // 10**n % 10


def group_total(grid, x, y, square_size):
    group_sum = 0
    for i in range(square_size):
        for j in range(square_size):
            group_sum += grid[(i + y - 1), (j + x - 1)]
    return group_sum


def get_total(summed_area_table,xoffset, yoffset, square_size=3):
    bottom_right = summed_area_table[yoffset + square_size - 1, xoffset + square_size - 1]
    top_right = summed_area_table[yoffset - 1, xoffset + square_size - 1] if yoffset > 0 else 0
    bottom_left = summed_area_table[yoffset + square_size - 1, xoffset - 1] if xoffset > 0 else 0
    top_left = summed_area_table[yoffset - 1, xoffset - 1] if xoffset > 0 and yoffset > 0 else 0
    return bottom_right - top_right - bottom_left + top_left


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


def get_max_group_position(summed_area_table, grid_size, square_size):
    position_totals = []

    for xindex in range(grid_size - square_size):
        for yindex in range(grid_size - square_size):
            position_totals.append(((xindex + 1, yindex + 1), get_total(summed_area_table, xindex, yindex, square_size)))

    max_coord = ()
    max_total = 0

    for position in position_totals:
        if position[1] > max_total:
            max_total = position[1]
            max_coord = position[0]

    return max_coord, square_size, max_total


def create_summed_area(grid):
    """
    Part 1 algorithm was too slow for larger square sizes so I found out about summed-area tables. Pretty neat!
    My hackish attempt at creating a summed area table. Numpy probably has something for this but I wanted
    to understand the table better anyways.
    """
    summed_area_table = grid.copy()
    for y in range(grid.__len__()):
        for x in range(grid.__len__()):
            if y > 0:
                summed_area_table[y, x] = summed_area_table[y, x] + summed_area_table[y - 1, x]
    for y in range(grid.__len__()):
        for x in range(grid.__len__()):
            if x > 0:
                summed_area_table[y, x] = summed_area_table[y, x] + summed_area_table[y, x - 1]
    return summed_area_table


def get_max_for_all_squares(summed_area_table):
    grid_size_list = []
    for i in range(summed_area_table.__len__()):
        grid_size_list.append(get_max_group_position(summed_area_table, summed_area_table.__len__(), i + 1))

    max_index = 0
    max_value = 0

    for index, grid_size in enumerate(grid_size_list):
        if grid_size[2] > max_value:
            max_value = grid_size[2]
            max_index = index

    return grid_size_list[max_index]


input = 9445
grid_size = 300
grid = numpy.zeros((grid_size, grid_size), numpy.int32)
grid = set_power_levels(grid, input)
summed_area_table = create_summed_area(grid)

print(grid)
print(summed_area_table)
print('part 1', get_max_group_position(summed_area_table, summed_area_table.__len__(), 3))
print('part 2', get_max_for_all_squares(summed_area_table))

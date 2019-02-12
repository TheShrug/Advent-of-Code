import re
import collections
import numpy

numpy.set_printoptions(threshold=numpy.inf, linewidth=10000)

large_int = 9999999999

def integers_from_string(string):
    return list(map(int, re.findall(r'-?\d+', string)))


def get_bounds(points):
    min_x, max_x, min_y, max_y = large_int, 0, large_int, 0
    for point in points:
        if point.px < min_x:
            min_x = point.px
        if point.px > max_x:
            max_x = point.px
        if point.py < min_y:
            min_y = point.py
        if point.py > max_y:
            max_y = point.py
    return [max_x, min_x, max_y, min_y]


def simulate_second(star_points):
    for index, point in enumerate(points):
        star_points[index] = point._replace(px=point.px + point.vx, py=point.py + point.vy)
    return star_points


def get_points_at_smallest_area(points):
    for i in range(large_int):
        prev_points = points.copy()
        prev_bounds = get_bounds(points)
        prev_point_area = (prev_bounds[0] - prev_bounds[1]) * (prev_bounds[2] - prev_bounds[3])
        next_bounds = get_bounds(simulate_second(points))
        next_point_area = (next_bounds[0] - next_bounds[1]) * (next_bounds[2] - next_bounds[3])
        if next_point_area > prev_point_area:
            print(i)
            return prev_points
        print(next_point_area)


input = open("input.txt")

Point = collections.namedtuple('Point', 'px, py, vx ,vy')

points = []

for line in input:
    ints = integers_from_string(line)
    points.append(Point(*ints))

final_points = get_points_at_smallest_area(points)

final_bounds = get_bounds(final_points)

matrix = numpy.zeros((final_bounds[2] - final_bounds[3] + 1, final_bounds[0] - final_bounds[1] + 1), numpy.int16)

for point in final_points:
    matrix[final_bounds[2] - point.py][final_bounds[0] - point.px] = 1

print(numpy.rot90(matrix, 2))

from collections import defaultdict
from operator import itemgetter

serial_number = 1723
size = 3

def calculate_fuel_cell(serial_number):
    fuel_cells = defaultdict(int)
    for x in range(1, 301):
        for y in range(1, 301):
            rack_id = x + 10
            begin_power_level = rack_id * y
            increased_power_level = begin_power_level + serial_number
            multiplied_power_level = increased_power_level * rack_id
            hundreds_digit = multiplied_power_level // 100 % 10
            power_lever = hundreds_digit - 5
            fuel_cells[(x, y)] = power_lever + fuel_cells[(x - 1, y)] + \
                                 fuel_cells[(x, y - 1)] - fuel_cells[(x - 1, y - 1)]
    return fuel_cells

def square_value(fuel_cells, size):
    values = defaultdict(int)
    for x in range(1, 301 - size + 1):
        for y in range(1, 301- size + 1):
            x0, y0, x1, y1 = x - 1, y - 1, x + size - 1, y + size - 1
            values[(x, y)] = fuel_cells[(x1, y1)] + fuel_cells[(x0, y0)] - \
                             fuel_cells[(x0, y1)] - fuel_cells[(x1, y0)]
    return values

def find_value_by_size(fuel_cells, size):
    values = square_value(fuel_cells, size)
    key = itemgetter(1)
    largest_total_power = max(values.items(), key=key)
    return largest_total_power

def find_size(fuel_cells):
    key = itemgetter(1)
    return max([find_value_by_size(fuel_cells, s) + (s,) 
            for s in range(1, 301)], key=key)

fuel_cells = calculate_fuel_cell(serial_number)

# part one
print(find_value_by_size(fuel_cells, size))

# part two
print(find_size(fuel_cells))


import fileinput
import re
from collections import defaultdict

filename = 'six.data'
coordinates = [tuple(map(int, re.findall(r'\d+', line))) for line in fileinput.input(filename)]

xmin, xmax = min(x for x, y in coordinates), max(x for x, y in coordinates)
ymin, ymax = min(y for x, y in coordinates), max(y for x, y in coordinates)

def dist(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)

area = defaultdict(int)
infinite = set()
size = 0
for y in range(ymin, ymax + 1):
    for x in range(xmin, xmax + 1):
        ds = sorted((dist(x, y, cx, cy), i)
            for i, (cx, cy) in enumerate(coordinates))
        if ds[0][0] != ds[1][0]:
            area[ds[0][1]] += 1
            if x in [xmin, xmax] or y in [ymin, ymax]:
                infinite.add(ds[0][1])
        if sum(n for (n, g) in ds) < 10000:
            size += 1
for k in infinite:
    area.pop(k)

# part 1
print(max(area.values()))
# part 2
print(size)
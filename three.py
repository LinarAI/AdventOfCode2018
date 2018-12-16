import numpy as np
import fileinput, re

# part one
matrix = np.zeros((1050, 1050), dtype=int)
for line in fileinput.input('three.data'):
    id, x, y, w, h = map(int, re.findall(r'\d+', line))
    matrix[y : y + h, x : x + w] += 1
print(len(np.extract(matrix > 1, matrix)))

# part two
for line in fileinput.input('three.data'):
    id, x, y, w, h = map(int, re.findall(r'\d+', line))
    if (matrix[y : y + h, x : x + w] == 1).all(): print(id)
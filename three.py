import numpy as np

f = open('three.data','r')
line = f.readline()
matrix = np.zeros((1050, 1050), dtype=int)

while line:
    claim = line.strip()
    pos1 = claim.find('@')
    pos2 = claim.find(':')
    left, top = claim[pos1+2:pos2].split(',')
    width, height = claim[pos2+2:].split('x')
    left, top, width, height= int(left), int(top), int(width), int(height)
    matrix[top:top+height, left:left+width] += 1
    line = f.readline()

condition = matrix > 1
num = len(np.extract(condition, matrix))
print(num)

f = open('three.data','r')
line = f.readline()

while line:
    claim = line.strip()
    pos1 = claim.find('@')
    pos2 = claim.find(':')
    left, top = claim[pos1+2:pos2].split(',')
    width, height = claim[pos2+2:].split('x')
    left, top, width, height= int(left), int(top), int(width), int(height)
    if (matrix[top:top+height, left:left+width] == 1).all():
        print(claim)
    line = f.readline()
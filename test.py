import math
from random import *

while True:
    seatlist = [[randint(0,1) for row in range(5)]for col in range(5)]
    countones = 0
    for row in range(5):
        countones += seatlist[row].count(1)
    if (countones / 25) > 0.4:
        break 

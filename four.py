from collections import defaultdict
from operator import itemgetter
import fileinput
import re

countguard = defaultdict(int)
countminutes = defaultdict(lambda: defaultdict(int))
for line in sorted(fileinput.input('four.data')):
    minute = int(re.search(r':(\d+)', line).group(1))
    if '#' in line:
        guard = int(re.search(r'#(\d+)', line).group(1))
    elif 'asleep' in line:
        start = minute
    elif 'wakes' in line:
        end = minute
        for m in range(start, end):
            countguard[guard] += 1
            countminutes[guard][m] += 1

# strategy 1
key = itemgetter(1)
guard = max(countguard.items(), key=key)[0]
minutes = max(countminutes[guard].items(), key=key)[0]
print(guard * minutes)

# strategy 2
guardlist = []
for guard in countminutes:
    minute, guardmax = max(countminutes[guard].items(), key=key)
    guardlist.append((guardmax, guard*minute))
print(sorted(guardlist)[-1][-1])
from collections import defaultdict
import fileinput
import re

deps = defaultdict(set)
tasks = set()
for line in fileinput.input('seven.data'):
    a, b = re.findall(r' ([A-Z]) ', line)
    deps[b].add(a)
    tasks |= {a, b}

# part one
done = []
for _ in tasks: done.append(min(c for c in tasks if c not in done and deps[c] <= set(done)))
print(''.join(done))

# part two
done = set()
worker = [''] * 5
counts = [0] * 5
seconds = 0

while True:
    for i, count in enumerate(counts):
        if count == 1:
            done.add(worker[i])
        counts[i] = max(0, count - 1)
    while 0 in counts:
        i = counts.index(0)
        candidates = [c for c in tasks if deps[c] <= done]
        if not candidates:
            break
        task = min(candidates)
        tasks.remove(task)
        counts[i] = ord(task) - ord('A') + 61
        worker[i] = task
    if sum(counts) == 0:
        break        
    seconds += 1
print(seconds)
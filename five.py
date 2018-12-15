import fileinput

polymers = next(fileinput.input('five.data'))

def react(polymer):
    result = ['']
    for c in polymer:
        if c == result[-1].swapcase():
            result.pop()
        else:
            result.append(c)
    return ''.join(result)

# part one
print(len(react(polymers)))

# part two
print(min(len(react(polymers.replace(c, '').replace(c.upper(), '')))
    for c in set(polymers.lower())))
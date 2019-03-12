import fileinput

def parse(it):
    num_children, num_matadata = next(it), next(it)
    children = [parse(it) for _ in range(num_children)]
    matadata = [next(it) for _ in range(num_matadata)]
    return (matadata, children)

root = parse(map(int, next(fileinput.input('eight.data')).split()))

# part 1
def sum_matadata(node):
    matadata, children = node
    return sum(matadata) + sum(sum_matadata(x) for x in children)

print(sum_matadata(root))

# part 2
def cal_value(node):
    matadata, children = node
    
    return sum(matadata) if children else \
           sum(cal_value(c) * matadata.count(i+1) for i, c in enumerate(children))
         
print(cal_value(root))
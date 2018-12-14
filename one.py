f = open('str.data', 'r')
sum = 0
data = f.readline()
list = [0]
while data:
    num1 = int(data[1:].strip())
    op = data[0]
    if (op == '+'):
        sum = sum + num1
    else:
        sum = sum - num1
    if sum in list:
        print(sum)
        break
    list.append(sum)
    data = f.readline()
    if not data:
        f = open('str.data', 'r')
        data = f.readline()
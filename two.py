f = open('data-zh.txt', 'r')
data = f.readline()
count2, count3 = 0, 0

while data:
    str = data.strip()
    booltwo = False
    boolthree = False
    for i in str:
        num = str.count(i)
        if (num == 2):
            booltwo = True
        elif (num == 3):
            boolthree = True
    if booltwo: count2 += 1
    if boolthree: count3 += 1
    data = f.readline()

print(count2 * count3)
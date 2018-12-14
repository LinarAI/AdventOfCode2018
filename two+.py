f = open('two.data', 'r')
data = f.readline()
ids = []
while data:
    nowid = data.strip()
    for ID in ids:
        diffnum = 0
        for pos in range(len(ID)):
            if ID[pos] != nowid[pos]:
                diffnum += 1
            if diffnum > 1:
                break
        if diffnum == 1:
            print(nowid)
            print(ID)
    ids.append(nowid)
    data = f.readline()

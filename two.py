changeList = list()
changeList.append("one")
changeList.append("Two")
changeList.append("Three")
changeList.append("Four")

changeList.append([i ** 2 for i in range(10)])
print(changeList)
for item in changeList:
    if isinstance(item, list):
        for i in item:
            print(i, end=' ')
    else:
        print(item, end=' ')


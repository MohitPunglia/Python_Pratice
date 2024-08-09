a = [1, 2, 3, 4, 1, 1, 3, 2, 9]

newlist = []

for i in a:
    if i not in newlist:
        newlist.append(i)
print(newlist)

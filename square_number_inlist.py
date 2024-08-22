#Python code to turn every item of a list into it's square.

l = [1, 3, 4, 5, 87, 43, 64, 98, 54, 40]

newl = []

for i in range(0,len(l)-1):
    newl.append(l[i] * l[i])
    
print(newl)

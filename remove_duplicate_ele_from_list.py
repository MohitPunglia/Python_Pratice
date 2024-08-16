# WAP to remove duplicate element from the list

l1 = [1, 1, 1, 2, 2, 45, 65, 65, 45, 3, 2, 1]

l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)

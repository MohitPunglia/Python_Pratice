# Python program to check whether the list is sorted or not with using sort() function.


l = [1, 2, 3, 4, 5]

flag = 0

for i in range(0, len(l) - 1):
    if l[i] >= l[i + 1]:
        flag = flag + 1
        break

if flag == 0:
    print("List is sorted")
else:
    print("List is not sorted")

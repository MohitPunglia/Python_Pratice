# Write a python program to reverse words in a string.

a = input("Enter your string : ")

a.split()

rev = []

for i in range(len(a) - 1, -1, -1):
    rev.append(a[i])
y = " ".join(rev)
print(y)

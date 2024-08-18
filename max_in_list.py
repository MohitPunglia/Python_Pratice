# Python program to print the maximum value of a given list without using the max() function.

l = [1, 9, 4, 3, 43, 2, 9]

max = l[0]

for i in l:
    if i > max:
        max = i

print(max)

# Python program to search a number in a given list.

l = [1, 3, 4, 5, 9, 0, 8, 7, 5, 4, 3, 23, 24, 65, 87, 43, 64, 98, 54, 40]

user_input = int(input("Enter Number to find in List : "))

for i in l:
    if i==user_input:
        print("True")
        break
else:
    print('False')


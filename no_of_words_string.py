# Python program to find number of words in a string.

str = input("Enter the String : ")

count = 0

for i in str:
    if i == " ":
        count = count + 1

words = count + 1

print(words)

# WAP to find occurance of charcter in the given string

S1 = input("Enter the number : ")
c1 = input("Enter number to find count in given number : ")

count = 0

for i in S1:
    if i in c1:
        count = count + 1

print(count)

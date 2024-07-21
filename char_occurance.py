# WAP to find occurance of charcter in the given string

S1 = input("Enter the string : ")
c1 = input("Enter Charcter to find count in given string : ")

count = 0

for i in S1:
    if i in c1:
        count = count + 1

print(count)

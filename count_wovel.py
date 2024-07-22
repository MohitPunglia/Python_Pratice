# WAP to count number of vowels in the given string

S1 = input("Enter the string :")
volwels = "aeiou"
count = 0

for i in S1:
    if i in volwels:
        count = count + 1

print(count)

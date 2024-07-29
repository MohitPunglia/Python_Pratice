# WAP to reverse a number

number = input("Enter number to reverse : ")

reverse = 0

for i in number:
    rem = int(number) % 10
    number = int(number) / 10
    reverse = (reverse * 10) + rem
    
print(reverse)

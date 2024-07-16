# WAP to check number is divisible by 3 & 9

number=int(input("Enter number to check if divisible by 3 & 9 : "))

if number // 3 == 0 and number // 6 == 0:
    print(number, " is divisible")
else :
    print(number," is not divisible")

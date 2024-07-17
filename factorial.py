# WAP to find factorila of number

num = int(input("Enter number to find factorial of : "))

a = 1

for i in range(1, num + 1):
    a = a * i

print("Factorial of", num ,"is : " , a )

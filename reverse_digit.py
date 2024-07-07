# Write a program to reverse a number entered by user

num=int(input("Enter number to reverse : "))

rev=0

for _ in str(num):
    a=num%10
    rev=rev*10 + a
    num=num//10

print(rev)






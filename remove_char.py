#WAP to remove a particular character from string

a = input("Enter String : ")
b = int(input("Enter value of character : "))
c = a[0 : b - 1]
d = a[b:]
print(c + d)

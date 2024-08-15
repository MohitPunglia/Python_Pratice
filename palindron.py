# WAP to check whether given string is palindron or not

a = input("Enter string : ")

rev = ""

for i in range(len(a) - 1, -1, -1):
    rev = rev + a[i]

print(rev)

if rev == a:
    print("String is palindrom")
else:
    print("String is not palindrom")

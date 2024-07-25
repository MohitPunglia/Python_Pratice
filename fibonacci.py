num = int(input("enter number : "))
f = 0
s = 1
l = 0
for i in range(num):

    l = f + s
    f = s
    s = l
    print(l,end=" ")

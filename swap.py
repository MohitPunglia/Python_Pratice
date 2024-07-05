#WAP to swap 2 numbers using 3rd variable
a=int(input('Enter 1st number : '))
b=int(input('Enter 2nd number : '))


def swap(a,b):
    c=b
    b=a

    print("value of a is ",c)
    print("value of b is ",b)
    

swap(a,b)

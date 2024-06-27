#Higher order function

l=[1,2,3,4]

def return_sum(func,l):
    result=0

    for i in l:
        if func(i):
            result=result+i

    return result


even=lambda sum:sum%2==0
odd=lambda sum: sum%2!=0
add=lambda sum: sum%3==0


print(return_sum(even,l))
print(return_sum(odd,l))
print(return_sum(add,l))

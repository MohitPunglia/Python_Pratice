l=[1,2,3,4,5,6,7]

a=filter(lambda x:x>4,l)

print(list(a))

fruits=['Apple','Orange','Banana','Mango']

b=filter(lambda fruit: 'o' in fruit,fruits )

print(list(b))

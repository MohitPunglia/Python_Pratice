class Customer:

    def __init__(self,name,age):
        self.name=name
        self.age=age

c1=Customer('Mohit',23)
c2=Customer('Rohit',19)
c3=Customer('Tom',34)

l=[c1,c2,c3]

for i in l:
    print(i.name,i.age)


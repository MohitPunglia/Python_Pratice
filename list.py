cities=['London','Paris','New York']
print(cities)

cities.append('Athenes')
print(cities)

cities[1]='Oslo'
print(cities)
print(cities[2])

contries=['UK','France','USA','Greece']
print(cities + contries)

print(len(cities))
print(cities.sort())
print(cities)


sample="how are you?"
print(sample.split())
print(sample.capitalize())
L=[]
for i in sample:
    print(i)
    L.append(i.capitalize())

print(L)
print(" ".join(L))

email="abc@gmail.com"
print(email[:email.find('@')])
print(email)

#Remove duplicate from List
number1=[1,1,1,13,5,5,5,6,0,4]
number=[]
for i in number1:
    if i not in number:
        number.append(i)

print(number)

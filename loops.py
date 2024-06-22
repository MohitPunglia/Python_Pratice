number = int(input("Enter number : "))

i=1

while i<11:
    print(i*number)
    i +=1 

#For loop

# range function
print(list(range(1,10)))

print(list(range(5)))

print(list(range(1,11,2)))

print(list(range(10,0,-1)))

#Sequence - order
print('London')
print('London','Paris')

for i in range(1,10):
    print(i)
print("----------------------------")
for i in range(1,10,2):
    print(i)
print("----------------------------")
for i in 'London':
    print(i)
print("----------------------------")
for i in [5,6,7,8]:
    print(i) 

#Nested Loops
rows=int(input("Enter number of rows to be printed : "))
for  i in range(1,rows):
    for j in range (0,i):
        print('*',end=' ')

    print ("")
        
    

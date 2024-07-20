# Python program to find the largest age among the three persons

person1=int(input("Enter age for 1st person : "))

person2=int(input("Enter age for 2nd person : "))

person3=int(input("Enter age for 3rd person : "))


def find_oldest(age1,age2,age3):
    if(person1==person2==person3):
        print("All person have same age")
    elif(person1==person2):
        print('Person 1 and Person 2 have same age')
    elif(person2==person3):
        print('Person 2 and Person 3 have same age')
    elif(person1==person3):
        print('Person 1 and Person 3 have same age ')
    elif(person1>person2 and person1>person3 ):
        print("Person 1 is oldest")
    elif(person2>person3):
        print('Person 2 is oldest')
    else:
        print('Person 3 is oldest')

find_oldest(person1,person2,person3)

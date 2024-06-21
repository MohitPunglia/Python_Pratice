email=input("Enter you email address " + ": " )

if '@' in email:
    password=input("Enter your password "  + ": ")

if email=='dummy@gmail.com' and password=='1234' :
    print("Welcome")

elif email=='dummy@gmail.com' and password != '1234' :
    print('Incorrect password')
    password=input("Re enter your password "  + ": ")

    if password =='1234' :
        print('Correct password - Welcome!!')
    
    else:
        print('Again incorrect password ')

else : 
    print('Incorrect credentials')

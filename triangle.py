# WAP to find given 3 angle can form a triangle or not

angle1=int(input("Enter 1st angle : "))

angle2=int(input("Enter 2nd angle : "))

angle3=int(input("Enter 3rd angle : "))

if angle1 + angle2 + angle3 == 180 :
    print("Triangle can be formed")
else :
    print("Triangle can't be formed")

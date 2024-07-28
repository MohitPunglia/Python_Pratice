number = int(input("Enter the number to find factor: "))

for i in range(1, number + 1):
    if number % i == 0:
        print("Factors are : ", i)

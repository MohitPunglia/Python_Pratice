# WAP to conver a given string into title case without using title() function

s1 = "ThIS IS string wHICH WE WANT TO coNVERT"

print("Original String : ", s1)

s2 = s1.split()

s3 = ""

# print(s2)

for i in s2:
    s3 = s3 + i[0].upper() + i[1:].lower() + " "

print("Converted String : ", s3)

#lambda input:expression 
"""Difference between Lambda and Functinons
1. Lambda has no return value 
2. Lambda return function rather than value
3. Lamda is used in one line 
4. Lamda has no name
"""

a=lambda x:x*2
print(a(2))

b=lambda x,y:x+y
print(b(2,3))

c=lambda x:'Even' if x%2==0 else 'Odd'
print(c(5))

d=lambda i:i[0]=='a'
print(d('apple'))
print(d('orange'))



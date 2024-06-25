d={'Name':'Mohit','Id':'12','Salary':'3000'}
print(d)
print('-'* 25)
print(d['Name']) 
print('-'* 25)

"""
1.Dictionary has no indexing 
2.Dictinary is a mutable  type
3.Keys are immutable and values can be mutuable 
4.Keys should be unique
"""

_2d={'Name':'Mohit','College':'MIT','Marks':{'M1':'56','M2':'85','M3':'75'}}
print(_2d)
print(_2d['Marks']['M2'])
print('-'* 25)


d['Id']='23'
print(d)
print('-'* 25)
print(d.get('Name'))
print('-'* 25)
d['Age']='23'
print(d)
print('-'* 25)


for i in d:
    print(i,d[i])

print('Mohit' in d)
print('Name' in d)

print('-'* 25)

for i in _2d:
    print(_2d.keys(), _2d.values())

print('-'* 25)

for i in d:
    print(d.keys(),d.values())

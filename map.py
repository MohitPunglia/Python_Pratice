l=[1,2,3,4,5]
a=list(map(lambda x:x*2,l))
print(a)



students=[  
     {  
      'name':'Ram',
      'gender':'Male',
      'physics':78
     },
   {  
      'name':'Murugan',
      'gender':'Male',
      'physics':34
   },
   {  
      'name':'Jenifer',
      'gender':'Female',
      'physics':67
   }
]


print(list(map(lambda student:student['name'],students)))

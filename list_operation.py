'''
      Python list CRUD operation
'''
l1 = ['paritosh','mca','paritoshrock@gmail.com']
print(l1[0])

#add element at last 
#without variable 
l1.append(9090990)
print(l1)
#with additional variable
house_no = 161_55_2
l1.append(house_no)
print(l1)


#add element at specified index
#without variable 
l1.insert(1,'section-B')
print(l1)
#with variable 
roll_no = "IC-2K20-51"
l1.insert(0,roll_no)
print(l1)

#deletion of element 
#pop delete at last lifo
l1.pop()
print(l1)
#remove at specified values
l1.remove('IC-2K20-51')
print(l1)


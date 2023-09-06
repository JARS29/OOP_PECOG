
grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}     #Creates a dictionary
print(grades)                     
print(grades['John'])                                           #Print values of the key 'John'
#grades['Sylvan']
grades['Sylvan'] = 'A'                                          #Asking a new key 'Sylvan' with th value A
print(grades)
print('John' in grades)                                         #Asking for Jhon in the dictionary
print('Daniel' in grades)                                       #Asking for Daniel in the dictionary
del(grades['Ana'])                                              #Removing Ana of the dictionary
print(grades)
print(grades.keys())                                            #Print the keys
print(grades.values())                                          #print the values


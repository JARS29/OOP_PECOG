# List

#  indexs   0    1    2    3
my_list = ['a', 'b', 'c', 'd']

print(my_list[0])  # Print the first element of the list
print(my_list[2])  # Print the third element of the list


len(my_list)                 #return the length of the list
my_list[-1]                  #return the last object of the list
my_list[2:]                  #return the last two objects
my_list[:2]                  #return the first two objects
#my_list[7]                   #return an error (number is out of the index)
my_list[0] = 123             #assign the new value at the position 0 (first)

# List methods

L1 = ['a' ,1 , 2]       #create a list with three element
print(L1)
L1.append(40)           #add 40 at the end of the list
print(L1)
L1.extend([1,2,3])      #add 1,2,3  at the end of the list
print(L1)
L1.append([1,2,3])      #SEE the difference with the previous one
print(L1)
L1.sort()               #Sort the list numerically
print(L1)
L1.reverse()            #change the order of the list
print(L1)
L1.remove(2)            #Delete the number 2 in the list (the first that is found)
print(L1)
L1.pop()                #Delete and return the last element of the list
print(L1)
L1.count(40)            #Counts how many times is 40 in the list
print(L1)
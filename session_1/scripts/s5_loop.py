# Loop

# For

for i in range(10): # For each number in the range of 0 to 10 do what is bellow
	print('i is equal to', i)


my_list = [1, 3, 5, 7, 9]  # Create a list of numbers

for i in my_list: # For each element in the variable my_list do what is bellow
	value = i * 2
	print('value',value)


lower = 10
upper = 20
# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))
print("Prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper + 1):
   for i in range(2,num):
      if (num % i) == 0:
         break
      else:
         print '%d is a prime number \n' %(num),



# While

count = 10

while count > 0:  # While the variable count is greater than 0 do what is bellow
	print('count', count)
	count = count - 1





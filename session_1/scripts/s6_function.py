

# This function print a message and a number
def my_first_function(message, number):
	print(message)
	print(number)


# This function sum a list of number e return it
def sum_numbers(numbers):
	count = 0
	for number in numbers:
		count = count + number
	return count


# Testing the functions

number_list = [2,4,6,8]
result = sum_numbers(number_list)
my_first_function('This is the sum result', result)
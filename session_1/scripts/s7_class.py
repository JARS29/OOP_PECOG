

# Creating the class Person
class Person:

	def __init__(self, name):
		# The properties of the person will be the variables that have self. at first
		self.name = name
		self.age = 0
		self.height = 0.3

	# What the Person does will be the functions

	def show_informations(self):
		print('\nInformations:')
		print('Name', self.name)
		print('Age', self.age)
		print('Height', self.height, 'meters')

	def make_birthday(self):
		self.age = self.age + 1
		self.grow_up(0.07)

	def grow_up(self, meters):
		if self.age < 21:
			self.height = self.height + meters


person1 = Person('Maria')
for i in range(25):
	person1.show_informations()
	person1.make_birthday()





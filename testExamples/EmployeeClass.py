class Employee(object) :
	raisePerc = 1.04

	def __init__(self, firstName, lastName) :
		self.firstName = firstName
		self.lastName = lastName

	@property
	def email(self) :
		return '{}.{}@gmail.com'.format(self.firstName, self.lastName)

	@property
	def fullName(self) :
		return '{} {}'.format(self.firstName, self.lastName)

	@fullName.setter
	def fullName(self, name) :
		firstName, lastName = name.split(' ')
		print('name passed is', name)
		self.firstName = firstName
		self.lastName = lastName

	@fullName.deleter
	def fullName(self) :
		self.firstName = None
		self.lastName = None		

	def __repr__(self) :
		return ('Employee: {} {}'.format(self.firstName, self.lastName))

	def __str__(self) :
		return ('{}, {}, {}, {}'.format(self.lastName, self.firstName, self.email, self.fullName))

	def __add__(self, other) :
		return self.firstName + other.firstName


# MAIN starts here...
emp_1 = Employee('John', 'Smith')
emp_1.firstName = 'Spencer'
print(emp_1.email, emp_1.fullName)

emp_1.fullName = 'NavinX Kumar'
print('new name is', emp_1.firstName)

del emp_1.fullName
print(emp_1.firstName)
#print(len(emp_1.firstName))
print(emp_1)
#print('simple call', emp_1)


#emp_other = Employee('Mike', 'Turner')
'''

print('repr call  ', repr(emp_1))
print('repr call 1', emp_1.__repr__())

print('str call', str(emp_1))
print(isinstance(Employee, object))
print(issubclass(Employee, object))

print emp_1.__add__(emp_other)
print (emp_1 + emp_other)
'''
#print(__class__(Employee))
#print(help(emp_1))
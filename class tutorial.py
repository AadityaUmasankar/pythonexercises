class Employee:

	def __init__(self,first,second,pay):
		self.first = first
		self.second = second
		self.pay = pay
		self.email = first + '.' + second + '@company.com'
		self.fullname = first + ' ' + second

	# def fullname(self):
	# 	return '{} {}'.format(self.first,self.second)

emp1 = Employee('Aaditya','Umasankar',1500000)

print(emp1.fullname)



    	


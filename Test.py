print('Welcome to Python Testing Programs !!!')
#Pattern Programing 
def oddNunber(value):
	print('{0} Printing All the Odd value from range {1}'.format('#'*10 , '#'*10))
	for i in value:
		if(i%2 != 0):
			print(i)
#Creating range of number. creting list of number start from o to  20
values = range(20)
#Calling function 
oddNunber(values)
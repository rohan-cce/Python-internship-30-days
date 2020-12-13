
filename = 'exception_data.txt'
# Outer try block catches file name or file doesn't exist errors.
print("First Example : Files")
try:
	with open(filename) as fin:
		for line in fin:
			items = line.split(',')
			total = 0
			# Inner try bock catches integer conversion errors.
			try:
				for item in items:
					num = int(item)
					total += num
				print('Total = ' + str(total))
			except:
				print('Error converting to integer. ', items)
except:
	print('Error opening file. ' + filename)
	
finally:
	print('This is our optional finally block. Code here will execute no matter what.')
	
print("--------------------------------------------------------------------------------------")
print("Second Example : ")	
# Second example: name Error type in except block; call function from try block.
def this_fails():
	x = 1/0
try:
	this_fails()
except ZeroDivisionError as err:
	print('Handling run-time error:', err)
	

def divide_me(n):
	x = 1/n

i = int(input('enter a number '))
try:
	divide_me(i)
except Exception as e:
	print(e)  # this will print the error msg but don't kill the execution of program
else:
	print('Your Code Run Successfully') # this will execute if divide_me(i) run sucessfully without an error
finally:
	print('thanks') # this will execute in every condition
print("-------------------------------------------------------------------------------------")
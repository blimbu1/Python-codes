def function():
	def add(a,b):
		print ("Sum is %d"%(a+b))
	return add

	
f =function()
f(2,7)
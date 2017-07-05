class Ons:
	def message(self):
		print("hello my friends")
		self.add(7,3)
	
	def add(self,b,c):
		d = b+c
		print("The output is %d "%d)

		
ref = Ons()
ref.message()
ref.add(10,200)
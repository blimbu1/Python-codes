class Two:
	def add_multi(self,*a):
		s = 0
		for i in a:
			s+=i
		print ("The total is %d"%s)

		
jam = Two()
jam.add_multi(4,5,6,7,8)
class First:
	def __init__(this):
		this.__phy = 0
		this.__che = 0
		this.__mat = 0
		this.__count = 0
		this.check = 0
	
	def physics(me,p):
		if (p>=0 and p<=150):
			me.__phy = p
			if me.__phy < 80:
				me.__count = me.__count + 1
		else:
			print("Enter number in range 0 to 150")
			me.check = 1
	
	def chemistry(me,c):
		if(c>=0 and c<=150):
			me.__che = c
			if me.__che<80:
				me.__count = me.__count + 1
		else:
			print("Enter number in range 0 to 150")
			me.check = 1
			
	def maths(me,m):
		if (m>=0 and m<=150):
			me.__mat = m
			if me.__mat<80:
				me.__count = me.__count + 1
		else:
			print("Enter number in range 0 to 150")
			me.check = 1
	
	def __calculations(self):
		self.__total = self.__phy + self.__che + self.__mat
		self.__percentage = (self.__total/450)*100 
		return self.__total, self.__percentage
	
	def show_results(this):
		if this.check ==0:
			if this.__count == 0:
				tot , per = this.__calculations()
				print("Mark entered for physics: %d"%this.__phy)
				print("Mark entered for chemistry: %d"%this.__che)
				print("Mark entered for Maths: %d"%this.__mat)
				print("The total is: %d"%this.__total)
				print("The percentage is %d"%this.__percentage)
			elif this.__count == 1:
				print("Friend you need to retake one exam")
			elif this.__count == 2:
				print("Friend you need to resit the entire course")
			elif this.__count == 3:
				print ("Friend just go home")
			

limb = First()
limb.physics(100)
limb.chemistry(132)
limb.maths(50)
limb.show_results()

	
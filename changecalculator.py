class Change:
	'''This class uses built in currency denominators to calculate the change that should be given out'''
	
	def __init__(self,x,y,z='pound'):
		'''This method initialises the number entered'''
		self.bill = x
		self.note = y
		self.ans = {}
		self.currency = z
	
	def calculateChange(self):
		return (self.note - self.bill)
		
	def currencyDenom(self):
		dict = {'pound':[50.0,20.0,10.0,5.0,2.0,1.0,0.50,0.20,0.10,0.05,0.02,0.01],'us':[100.0,50.0,20.0,10.0,5.0,2.0,1.0,0.50,0.25,0.1,0.05,0.01],
		'nepalese':[1000.0,500.0,100.0,50.0,20.0,10.0,5.0,2.0,1.0,0.5,0.2,0.1,0.02,0.01]}
		return dict[self.currency]
		
		
		
	def doMath(self):
		j = self.currencyDenom()
		print("j = ",j)
		change = self.calculateChange()
		print("change = %0.2f"%change)
		dividers = [i for i in j if i<=change]
		print("dividers = ",dividers)
		for b in dividers:
			if change//b >=1 :
				self.ans[b] = change//b
				change = round((change%b),2)
				print("change =%0.2f "%change)
				
				
c = Change(2.5,10)
c.doMath()
print(c.ans)
		
	

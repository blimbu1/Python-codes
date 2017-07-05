first = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

third = {'1':{'0':'ten','1':'eleven','2':'twelve','3':'thirteen','4':'fourteen','5':'fifteen','6':'sixteen','7':'seventeen','8':'eighteen','9':'nineteen'},2:{'2':'twenty','3':'thirty','4':'fourty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'},3:'hundred',4:'thousand'}

number = input("Enter number ")
ans =""
length = len(number)
for j in number:
	if length == 4:
		ans = ans + first[j] +" "+ third[length]
	if length == 3:
		ans = ans +" " if j=='0' else ans+" " + first[j] +" "+ third[length]+" "
		ans = ans + "and"+" "
	if length == 2:
		if j=='1':
			ans = ans + third[j][number[-1]]+" "
			length=0
		elif j=='0':
			ans = ans +" "
		else:
			ans = ans + third[length][j]+" "
	if length == 1:
		ans = ans + first[j]+" "
	length =length -1

print(ans)		
	
	


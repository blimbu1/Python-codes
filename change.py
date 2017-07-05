bill = input("Enter the bill amount: ")
notes = input("Enter the denomination used to pay: ")

change = float(notes) - float(bill)
change = round(change,2)
ans = {}

pound = [50.0,20.0,10.0,5.0,2.0,1.0,0.50,0.20,0.10,0.05,0.02,0.01]

print ("The changes is %0.2f" %change)

for j in [y for y in pound if y<=change]:
	if change//j >= 1.0:
		ans[j] = change//j
		change = round((change %j),2)
		print("%0.2f = %0.2f"%(j,ans[j]))
		
"""for val in ans.keys():
	print ("£%0.2f : %0.2f"%(val, ans[val])"""

print(ans)
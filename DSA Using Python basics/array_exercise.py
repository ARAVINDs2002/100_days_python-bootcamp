expenses=[2200,2350,2600,2130,2190]
#how many dollar spend extra when compared to jan
jan=expenses[0]
feb=expenses[1]
print(feb - jan)
#total expence in 1st quarter 3months
total_expense=expenses[0]+expenses[1]+expenses[2]
print(total_expense)
#find out if you spend 2000 dolaer in nay month
found=False
for i in expenses:
    if i==2000:
        print("found")
        found==True
        break
if found==False:
    print("not") 
#adding 1980 as the expence of 5th month
expenses.append(1980)
print(expenses)
#got a refund of 200 dollar for an item i bought in april update the cost in april
expenses[5]+=200
print(expenses)

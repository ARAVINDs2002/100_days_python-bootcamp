bills=["Electricity_Bill","Water_Bill","House_Holds","Travel_Expences"]#btw you can add your own bills here
sum=0
print("|---------------------------------------------------|")
print("|       E X P E N C E   C A L C U L A T O R         |")
print("|---------------------------------------------------|")
for each_bills in bills:
    print(f"enter amount for this month's {each_bills} :")
    amt=int(input())
    sum+=amt
print(f"you have a total expence of rupess {sum}")


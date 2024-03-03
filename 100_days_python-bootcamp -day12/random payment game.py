import random as rn
cards=['card1','card2','card3','card4','card5']
lot=0
for i in range (1):
    print("roling the dice !!!!")
whom_to_pay=rn.choice(cards)
if whom_to_pay=='card1':
    print("rogue has to pay...awwww!")
elif whom_to_pay=='card2':
    print("jimmye has to pay...awwww!")
elif whom_to_pay=='card3':
    print("andriyana has to pay...awwww!")
else:
    print("thosan has to pay....awww!")

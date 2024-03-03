import random as rn
choice=int(input("enter the choise (0 for rock 2 for scissor 5 for paper):"))
pc=[0,2,5]
random=rn.choice(pc)
if choice==0 and random==2 or choice==5 and random==0 or choice==2 and random==5:
    print(f"you win !!!!machine used {random}")
else:
    print(f"machine wins!!! machine used {random}")
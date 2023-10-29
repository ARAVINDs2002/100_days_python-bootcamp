import random as rn
print("what do do pick to play stone(0) paper(5) or scissor(2)")
sys_choice=[0,5,2]
user_choice =int(input())
stone= ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper=  ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissor=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print(f"you choose.....\n")
if user_choice==0:
  print(stone)
elif user_choice==5:
  print(paper)

elif user_choice==2:
  print(scissor)
else:
  print("no such symbol is there!!!")


if user_choice in sys_choice:
  system_choice=rn.choice(sys_choice)
  print("the system chose....")
  if system_choice==0:
    print(stone)
  elif system_choice==5:
    print(paper)

  elif system_choice==2:
    print(scissor)
else:
  print("you didnt play accoording to the rules !!!")
  

if user_choice==0 and system_choice==2:
  print("you won!!!")

elif user_choice==5 and system_choice==0:
  print("you won!!!")

elif user_choice==2 and system_choice==5:
  print("you won!!!")
else:
  print("you lose!!!")




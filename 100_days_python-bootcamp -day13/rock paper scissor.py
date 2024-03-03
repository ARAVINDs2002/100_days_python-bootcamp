#rock paper scisor
import random as rn    #0 for stone✊
                       #1 for paper 🖐️
                       #2 for scissor ✌️


game_choises=[0,1,2]

user_choice=int(input("enter your choise ( 0 for stone✊ | 1 for paper 🖐️| 2 for scissor ✌️)  :"))
pc_choices=rn.choice(game_choises)
if user_choice==pc_choices :
    print("we are draw both used the same")
elif user_choice<pc_choices:
    print(f"pc wins pc used {pc_choices}!!!")
else:
    print(f"you win pc used {pc_choices}!!!")

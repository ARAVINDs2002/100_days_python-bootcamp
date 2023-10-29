names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random as rn
length=len(names)
choice=rn.randint(0,length-1)
choicename=names[choice]
print(f"{choicename} is going to buy the meal today!")
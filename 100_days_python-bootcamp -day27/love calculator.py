yourname = input("Enter your name: ")
lovname = input("Enter his/her name: ")
concat = yourname + lovname

print(f"Your name is {yourname}")
print(f"Your lover's name is {lovname}")

t = concat.count('t')
r = concat.count('r')
u = concat.count('u')
e = concat.count('e')
true = t + r + u + e

l = concat.count('l')
o = concat.count('o')
v = concat.count('v')
e = concat.count('e')
love = l + o + v + e

lovescore = true + love

if lovescore > 70:
    print("Hey, you are like bread and jam!")
elif 50 > lovescore and lovescore < 70:
    print("It's okay, no big deal...")
else:

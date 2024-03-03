import random as rn

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

password = []

num = int(input("How many numbers do you want? "))
alp = int(input("How many letters do you want? "))
sym = int(input("How many symbols do you want? "))


for _ in range(alp):
    ch = rn.choice(alphabets)
    password.append(ch)


for _ in range(num):
    ch = rn.choice(numbers)
    password.append(ch)


for _ in range(sym):
    ch = rn.choice(symbols)
    password.append(ch)

rn.shuffle(password)


password_str = ''.join(password)

print(password_str)



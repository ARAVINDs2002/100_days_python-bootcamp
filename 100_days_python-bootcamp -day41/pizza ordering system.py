print("|---------------------------------------------------------------|")
print("|              pizza order system                               |")
print("|--------------choose your pizza--------------------------------|")
print("|1) small pizza   - 30$    for extra cheese +20$ for every pizza|")
print("|2) medium pizza  - 60$                                           |")
print("|3) large pizza   - 80$                                           |")
print("|---------------------------------------------------------------|")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Thank you... it will be 30$")
    cheeseornot = input("Would you like to add cheese? (y/n): ")
    if cheeseornot == 'y':
        print("Thank you... it will be 30$ + 20$, so 50$")
    else:
        print("Thank you. Take your order.")
elif choice == 2:
    print("Thank you... it will be 60$")
    cheeseornot = input("Would you like to add cheese? (y/n): ")
    if cheeseornot == 'y':
        print("Thank you... it will be 60$ + 20$, so 80$")
    else:
        print("Thank you. Take your order.")
elif choice == 3:
    print("Thank you... it will be 80$")
    cheeseornot = input("Would you like to add cheese? (y/n): ")
    if cheeseornot == 'y':
        print("Thank you... it will be 80$ + 20$, so 100$")
    else:
        print("Thank you. Take your order.")
else:
    print("Invalid choice. Please select a valid option (1, 2, or 3).")


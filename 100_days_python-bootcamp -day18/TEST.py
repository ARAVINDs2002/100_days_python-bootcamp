def main():
   height=int(input("enter the height of the wall  :"))
   width=int(input("enter the width of the wall :"))
   area = height * width
   coverage=int(input("how much square meters will a paintcan covers? :"))
   num_of_can_needed=area//coverage
   print(f"num of can needed is{num_of_can_needed}")
main()

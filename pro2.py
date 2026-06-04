print ("...welcome to logic box...")

while True:

    print("\n select an option:")
    print("1. generate a pattern.")
    print("2. analyze a range of number.")
    print("3. exit")

    choice=input("enter your choice: ")

    if choice == "1":
        row=int(input("enter the number of rows for the pattern: "))

        if row <=0:
            print("invalid row count! row must be greater than 0.")
            break
        print("pattern")
        for i in range(1,row+1):
            for j in range(i):
                print("*",end="")
            print("")
    elif choice == "2":
        start=int(input("enter a start of range for analyse"))
        end=int(input("enter a end of range for analyse"))

        if end<start:
            print("end must be greater than start!!")
            continue
        total=0
        print()

        for num in range(start,end+1):
            if num ==0:
                pass
            if num%2==0:
                print(f"number {num} is even.")
            else:
                print(f"number {num} is odd.")
            total+=num
        print(f"\nsum of all numbers from {start} to {end} is: {total}")

    elif choice == "3":
        print("\n..exiting program..")
        break
    else:
        print("invalid choice!! pls select a valid option. ")

print("\n Thank you for using data organizer and displaying. ") 
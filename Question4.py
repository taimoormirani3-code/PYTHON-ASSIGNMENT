balance = 50000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Select an option: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        deposit = float(input("Enter deposit amount: "))
        balance = balance + deposit
        print("New Balance:", balance)

    elif choice == 3:
        withdraw = float(input("Enter withdrawal amount: "))

        if withdraw <= balance:
            balance = balance - withdraw
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance!")

    elif choice == 4:
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid option!")
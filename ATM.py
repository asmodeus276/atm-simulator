print("Welcome to the ATM")
balance =int(input("Enter your Balance: $"))
pin =int(input("Enter FOUR DIGIT PIN:"))
print("------LOGIN------")
correct_pin=int(input("Enter FOUR DIGIT PIN"))

if correct_pin==pin:
    print("Verified successfully")
    while True:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice=int(input("Enter your choice"))
        if choice==1:
            print("Your balance is:$",balance)
        elif choice==2:
            amount = int(input("Enter your amount:"))
            if amount>0:
                balance=balance+amount
                print("Your updated balance is:$",balance)
            else:
                print("invalid amount")
        elif choice==3:
            withdraw = int(input("Enter withdraw money:"))
            if withdraw>0 and withdraw<=balance:
                balance=balance-withdraw
                print("You can collect your cash")
                print("your remaining balance:$",balance)
            else:
                print("Invalid balance")
        elif choice==4:
            print("Thank you for using the ATM")
            break
        else:
            print("Invalid choice")
else:
    print("incorrect pin")            

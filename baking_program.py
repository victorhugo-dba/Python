# Python banking program

def Show_Balance(balance):
    print("*******************")
    print(f"Your balance is ${balance:.2f}")
    print("*******************")

def Deposit():
    print("*******************")
    amount = float(input ("Enter an amount to be deposited: "))
    print("*******************")

    if amount < 0:
        print("*******************")
        print("That's is not a valid amount")
        print("*******************")
        return 0
    else:
        return amount

def Withdraw(balance):
    print("*******************")
    amount = float(input("Ente amount to be withdraw: "))
    print("*******************")

    if amount > balance:
        print("*******************")
        print("Insufficient funds")
        print("*******************")
        return 0
    elif amount < 0:
        print("*******************")
        print("Amount must be greater tanh 0")
        print("*******************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*******************")
        print("Banking program")
        print("*******************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*******************")

        print("*******************")
        choice = input("Enter your choice (1-4): ")
        print("*******************")

        if choice == '1':
            Show_Balance(balance)
        elif choice == '2':
            balance += Deposit()
        elif choice == '3':
            balance -= Withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*******************")
            print("That is not a valid choice")
            print("*******************")
    print("*******************")
    print("Thank you! Have a nice day!")
    print("*******************")

if __name__ == '__main__':
    main()
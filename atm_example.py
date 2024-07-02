class Atm:

    def __init__(self):
        self.pin = "1234"
        self.balance = 0

        self.menu()

    def menu(self):
        user_input = input(
            """ 
        Hello, please select the below option to proceed:
        1.Enter 1 to create pin
        2.Enter 2 to deposit
        3.Enter 3 to withdraw
        4.Enter 4 to check balance
        5.Enter 5 to exit   
        ========================     
        """
        )

        if user_input == "1":
            self.create_pin()
            
        elif user_input == "2":
            self.withdraw()
           
        elif user_input == "3":
            self.deposit()
            
        elif user_input == "4":
            self.check_balance()
            
        else:
            print("Bye")

    def create_pin(self):
        self.pin = input("Enter your pin : ")
        print("Pin set successfully!!")

    def withdraw(self):
        temp = input("Enter your pin :")
        if temp == self.pin:
            withdraw_amount = int(input("Enter amount to withdraw :"))
            if withdraw_amount > self.balance:
                input("Balance not sufficent, please deposit money")
            else:
                self.balance = self.balance - withdraw_amount
                print(withdraw_amount, "Amount deposited")

    def deposit(self):
        temp = input("Enter your pin : ")
        if temp == self.pin:
            amount = int(input("Enter amount to deposit"))
            self.balance = self.balance + amount
        else:
            print("Incorrect pin")

    def check_balance(self):
        temp = input("Enter your pin : ")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid Pin")


sbi=Atm()

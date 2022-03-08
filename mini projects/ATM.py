import sys, random

class ATM_SYS:
    def __init__(self,customer,accountNo, balance=0):
        """customer is the name of holder
           accountNo speakes for itself
           so does balance
        """
        #print("Welcome to THINKTECH bank ")
        self.customer= customer
        self.accountNo= accountNo
        self.balance = balance

    def acc_info(self):
        print("\n--------ACCOUNT DETAILS--------")
        print(f"AccountHolder : {self.customer.upper()}")
        print(f"AccountNumber : {self.accountNo}")
        print(f"AccountBalance :{self.balance}\n")

    def depositCash(self,amount):
        self.amount = amount
        self.balance= self.balance + self.amount

    def withdrawCash(self, withdrawalAmount):
        # the  block of code below can be replaced with a try and exception block
        self.amount = amount
        if self.amount > self.balance:
            print("INSUFICIENT FUNDS") 
        # due to server failiure and hackers we have to test for negative numbers
        elif self.amount<0:
            print("ONLY POSITIVE NUMBERS")
        else:
            self.balance = self.balance - self.amount

        print(f"Nu.{self.amount} WITHDRAWN SUCESSFULLY")

    def transaction(self):
        print("""
             TRANSACTION
        ########################
        MENU
        1. Account Details
        2. Check Balance
        3. Deposit
        4. Withdraw
        5. Exit
        6. Print Receipt

        ########################
        """)
        while True:
            try:
                option=int(input("Enter the number of the option:"))
            except:
                print("ERROR:Enter numbers btween 1 and 5 ")
                continue
            else:
                if option==1:
                    self.acc_info()
                elif option==2:
                    self.acc_info()
                elif option==3:
                    amount= int(input("HOW MUCH DO YOU WANT TO DEPOSIT?:"))
                    self.depositCash(amount)
                elif option==4:
                    amount= int(input("HOW MUCH DO YOU NEED?:"))
                    self.withdrawCash(amount)
                elif option == 5:
                    print("THANKS FOR USING THINKTECH ATM SERVICE")
                
                    sys.exit()
                elif option==6:
                    self.PrintReceipt()

        def PrintReceipt(self):
            print("######## THINKTECH BANK #########")
            print(f"""
            GENERATING RECIEPT......
            ############################################################
                Transaction number: {random.randint(10000, 1000000)}
                Account holder: {self.name.upper()}
                Account number: {self.accountNo}
                Available Balance: Nu.{self.balance}


                THANKS FOR CHOOSING US AS YOUR ATM SERVICE PROVIDER
            ############################################################
            """)

print("########WELCOME TO THINKTECH BANK##########")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Would you like to open an account?")
reply = input("enter \'YES\' or \'NO\' : ")
y = ['YES','Yes','yes']
N = ['NO','No','no']
if reply in y:
    name= input("Enter your name Please:")
    accountNum= int(input("Enter any ten digit number for your Account Number :"))
    print("Congratulations! Your Account Have Been Created sucessfully.....\n")
elif reply in N:
    print("THANK YOU FOR USING OUR SERVICE")
    Print("Pleasr visit us soon ....")

NewCard = ATM_SYS(name, accountNum)

while 1==1:
    transaction= input("do you want to do any Account Transactions?(y/n):")
    if transaction =="y":
        NewCard.transaction()
    elif transaction== "n":
        print("""
    ---------------------------------------------------
     |  Thanks for choosing THINKTECK as your bank  |
         Visit us again!
        """)
        break
    else:
        raise("WRONG PARAMETER")
        
    




                


    

        

        
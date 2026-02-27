# Module 1:Authentication Module
password="1234"
attempts=3
for i in range(attempts):
    guess=input("Enter your password:")
    if guess==password:
        print("Permission garanted")
        break 
    elif  guess!=password:
        print("Invalid password")  
    else:
     print("Maximum attempts reached. Account Locked.")   

# Module 2:ATM Menu Control Module
# Module 3:Transaction Processing Module
# password="1234"
# guess=input("Enter your password:")
if guess==password:
    print("Authentication Successful")
    option=0
    balance=1000
    while  option!=4:
     print("1.Check Account Balance")
     print("2.Deposit Funds")
     print("3.Withdraw Funds")
     print("4.Exit System")
     option=int(input("Select an option(1-4):"))
     if option==1:
            print("Current Account Balance:",balance)
     elif option==2:
            deposit_amount=int(input("Enter deposit amount:"))
            balance=balance+deposit_amount
            print("Deposit Successful.")
            print("Updatd Balance:",balance)
     elif option==3:
            withdraw_amount=int(input("Enter withdrawl amount:"))
            if withdraw_amount<=balance:
                  balance=balance-withdraw_amount                  
                  print("Successful withdrawl")
                  print("Updated Balance:",balance)
            else:
             print("Transaction Failed: Insufficient Funds.")
     elif option==4:
            print("Thank You for using the ATM System.")
     else:
            print("Invalid option. Please try again.")
else:
    print("Wrong password. Access Denied.")

cardpassword= "12345"
balance=500000
right_to_try=3
print("""Welcome to Leyla's bank!
      card password=12345
      
      
      """)


situation=True


while situation:
    entered_password=input("Enter Card Password: ")
    if entered_password != cardpassword:
        print("Wrong password. Try again.")
        right_to_try -=1
        print(right_to_try,"Your Right to Try Remains")
        if right_to_try == 0:
            print("You no longer have the right to try.Your card has been blocked. Please Contact Bank..")
            situation=False
    else:
        while situation:
            print("Correct Password. Login Done.")
            print(""" 
                  Select the action to be taken
                  ----------------------------
             
                  1-Withdraw Money
                  2-Deposit
                  3-Balance inquiry
                  4-Exit
                  -----------------------------

                  """)
            while situation:
                transaction_number=input("Enter Transaction Number: ")
                if transaction_number=="4":
                    print("Checked Out")
                    situation=False
                    
            
                elif transaction_number =="3":
                    print("Total Balance", balance )
                elif transaction_number=="2":
                    amount_to_be_deposited=int(input("Enter the Amount to be Deposited: "))
                    balance += amount_to_be_deposited
                    print("Transaction Completed")
                elif transaction_number=="1":
                    amount_to_be_withdrawn= int(input("Enter the Amount to be Withdrawn: "))
                
                    if amount_to_be_withdrawn> balance: 
                        print("Insufficient Funds")
                    else:
                        balance-= amount_to_be_withdrawn
                        print("Transaction Completed")


           
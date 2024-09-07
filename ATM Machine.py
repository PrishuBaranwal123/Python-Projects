amount=10000
Password=2500
a="1"
while(a=="1"):
        pin=int(input("Enter the pin: "))
        if(pin==Password):
                choice=int(input("Press 1 to Credit,Press 2 to Debit,Press 3 to Check Balance,Press 4 to Password change: "))
                if(choice==1):
                        credit=float(input("Enter the amount you want to credit: "))
                        amount=amount+credit
                        print("Your amount is credited")
                        print("Your new balance is",amount)
                        print("Thank You for Using my ATM")
                        print("Press 1 to Countinue or something else to exit: ")
                elif(choice==2):
                        debit=float(input("Enter the amount you want to debit: "))
                        if(debit>amount):
                                print("Insufficiant balance")
                                print("Thank You for Using my ATM")
                                print("Press 1 to Countinue or something else to exit: ")
                        else:
                                amount=amount-debit
                                print("Your remaining balance is",amount)
                                print("Thank You for Using my ATM")
                                print("Press 1 to Countinue or something else to exit: ")
                elif(choice==3):
                        print("Your balance is: ",amount)
                        print("Thank You for Using my ATM")
                        print("Press 1 to Countinue or something else to exit: ")
                elif(choice==4):
                        Pincode=int(input("Enter the new Password: "))
                        print("Your Pin is successfully changed")
                        print("Thank You for Using my ATM")
                        print("Press 1 to Countinue or something else to exit: ")
                else:
                        print("Wrong Input given")
                        print("Thank You for Using my ATM")
                        print("Press 1 to Countinue or something else to exit: ")
        else:
                        print("Wrong password given") 
                        print("Thank You for Using my ATM")                       
        a=(input(""))
        if(a!=1):
                print("Thank you for using my ATM")
                print("Have a Good Day ")
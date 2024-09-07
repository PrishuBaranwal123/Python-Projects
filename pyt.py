# calculator
a="1"

while(a=="1"):
        num1=int(input("Enter the 1st value: "))
        operation=input("Press + for addition,- for subtraction,* for multiplication,/ for divition,// for floor divition,** for roots,% for Modules ")
        num2=int(input("Enter the 2nd value: "))
        
        if(operation=="+"):
                sum=num1+num2
                print("The sum is :",sum)
        elif(operation=="-"):
                sub=num1-num2
                print(" The sub is :",sub)
        elif(operation=="*"):
                multiplication=num1*num2
                print(" The multiplication is :",multiplication)
        elif(operation=="/"):
                if(num2==0):
                        print("Not define")
                else:
                 divide=num1/num2
                 print(" The divide is :",divide)
        
        elif(operation=="//"):
                divide2=num1//num2
                print(" The floor division is :",divide2)
        elif(operation=="**"):
                roots=num1**num2
                print(" The roots is :",roots)
        else:
                a=input("wrong operation ")
        
        a=input("Press 1 to countinue: ")
        print("Thank you for using my calc")
        
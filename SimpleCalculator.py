choice=0
while(choice!=6):
    print("Enter 1 for Addtion")
    print("Enter 2 for Subtraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division")
    print("Enter 5 for Remiander")
    print("Enter 6 for Exit")
    choice = int(input("Enter Choice Number:-"))
    if choice==1:
        num1 = int(input("Enter Number 1:-"))
        num2 = int(input("Enter Number 2:-"))
        add = num1+num2
        print("Addtion = ",add)
    elif choice==2:
        num1 = int(input("Enter Number 1:-"))
        num2 = int(input("Enter Number 2:-"))
        sub = num1-num2
        print("Subtraction = ",sub)
    elif choice==3:
        num1 = int(input("Enter Number 1:-"))
        num2 = int(input("Enter Number 2:-"))
        mul = num1*num2
        print("Multiplication = ",mul)
    elif choice==4:
        try:
            num1 = int(input("Enter Number 1:-"))
            num2 = int(input("Enter Number 2:-"))
            div = num1//num2
            print("Quiteint = ",div)
        except ZeroDivisionError:
            print("Number with zero is not divisible")
    elif choice==5:
        num1 = int(input("Enter Number 1:-"))
        num2 = int(input("Enter Number 2:-"))
        rem = num1%num2 
        print("Remaninder = ",rem)
    elif choice==6:
        print("--------------EXIT-----------------")
    else:
        print("Enter valid choice Please Try again")

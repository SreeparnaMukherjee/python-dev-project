#Simple Calculator
def calculator():
    while True:  
        print("Select operation:")#Operations that can be done by the calculator
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")


        choice=input("Enter your choice:")
        if choice in ("1","2","3","4"):
            try:
                x=float(input("Enter first number: "))
                y=float(input("Enter second number: "))
            except ValueError:
                print("Invalid input!\nPlease enter numeric values.")
                continue


            if choice=="1":
                print(f"Result:{x}+{y}=", x + y)# Addition
            elif choice == "2":
                print(f"Result:{x}-{y}=", x - y)# Subtraction
            elif choice == "3":
                print(f"Result:{x}*{y}=", x * y)# Multiplication
            elif choice=="4":
                print(f"Result:{x}/{y}=", x / y)# Division
        else:
            print("Invalid choice!\nPlease choose a valid option.")


        if choice == '5':
            print("Calculator closed")
            break


#Function calling
if __name__=="__main__":
    calculator()




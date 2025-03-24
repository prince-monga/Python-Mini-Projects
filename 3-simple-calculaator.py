#Simple calculator

#step:1 all calculation define in function

def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def multi(a,b):
    return a*b

def div(a,b):
    if b==0:
        return"Error: Zero se divide ni hota"
    return a/b


#step:2 Now, display the Symbolls (menu type)-- which type of operation can performed by user

#It can show every operations after then user exit value click then terminate the program



while True:
    print("\n*** Simple Calculator ***")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    
    choice=input("Enter Your choice (1-5)")
    
    if choice == "5":
        print("Exiting... GoodBye")
        break
    if choice in ("1","2","3","4"):
        try:
            num1=int(input("Enter First number: " ))
            num2=int(input("Enter First number: " ))
        except ValueError:
            print("invild input!")
            continue
        
        if choice =="1":
            print(f"Result: {num1}+{num2}= {add(num1,num2)}")
        elif choice =="2":
            print(f"Result: {num1}-{num2}= {sub(num1,num2)}")  
        elif choice =="3":
            print(f"Result: {num1}*{num2}= {multi(num1,num2)}")
            
        elif choice =="4":
            print(f"Result: {num1}/{num2}= {div(num1,num2)}") 
            
    
    else:
        print("invaild choice")
    
    
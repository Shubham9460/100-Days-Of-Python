import art

# Define math operation
def add(num1 , num2):
    return num1 + num2

def multiply(num1 , num2):
    return num1 * num2

def divide(num1 , num2):
    if n2 == 0:
        return "Error : Division by zero"
    return num1 / num2

def subtrect(num1 , num2):
    return num1 - num2

# operation dictionary
operation = {
    "+":add,
    "*":multiply,
    "/":divide,
    "-":subtrect
}


def calculator():
    print(art.logo)

    
    num1 = float(input("What is a first number"))

    should_continue = True
     
    while(should_continue):
        #print available operations
        for symbol in operation:
            print(symbol)
        operation_symbol = input("Pick a Opreation : ")
        num2 = float(input("What is a next Number ?"))

        
        result = operation[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        # Ask user whether to continue
        choice = input(f"Type 'Y' to contiue calculet with {result} , otherwish type 'n' to exit").lower()

        if choice == "y":
            num1 = result
        else:
            should_continue = False
            print("\n" * 30) # clear screen
            calculator()  #Restart fresh
            
calculator()

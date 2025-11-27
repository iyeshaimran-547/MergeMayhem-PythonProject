def Ayesha_Imran(): #function definition
    while True: 
    #Infinite loop so that the loop terminates only when user explicitly mentioned
        a = input("Enter first number or 'exit' to quit: ")
        if a.lower() == "exit":
        #makes input case-insensitive
            print("Calculator exited successfully!")
            break #breaks the loop
        b = input("Enter second number: ")
        operation = int(input("\nChoose an operation:\n"
                    "1. Add\n"
                    "2. Subtract\n"
                    "3. Multiply\n"
                    "4. Divide\n"))
        
        #handles input errors without crashing the program
        try: 
            a = float(a)
            b = float(b)
        except ValueError:
            print("Enter Valid Numbers!")
            continue

        if operation == 1:
            result = a + b
        elif operation == 2:
            result = a - b
        elif operation == 3:
            result = a * b
        elif operation == 4:
            if b == 0: #For displaying error at zero
                print("Math ERROR: Divsion by zero not allowed!")
                continue
            result = a / b
        else:
            print("Choose one of the given choices!")
        
        print(f"Result = {result}")
Ayesha_Imran() #function call
    
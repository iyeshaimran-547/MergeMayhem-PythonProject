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
import random  # Importing random module to generate a random number

def Tahreem_Zafar():
    while True:
         number = random.randint(1, 50)
         attempts = 0  # Counter to track number of guesses
         print("\nLet's Play:)")
         print("I thought of a number between 1 and 50")
         print("Try to make a guess!")

         while True:  # Infinite loop until user guesses the correct number
             guessInput = input("Enter your guess: ")
             # Check if input is digits only
             if not guessInput.isdigit():
                 print("Oops! Wrong :( , Try Again!")
                 continue
             guess = int(guessInput)  # Convert input to integer
             if guess < 1 or guess > 50:
               print("Invalid input! Enter a number BETWEEN 1 and 50.")
               continue

             attempts += 1 

             if guess < number:
              print("Too low! Make a Higher Guess")
             elif guess > number:
              print("Too high! Make a Lower Guess")
             else:
              print(f"Wow, Correct!!! The number was {number}.")
              print(f"You guessed it in {attempts} attempts.\n")
              break 

         print("Do you want to play again?")
         choice = input("Enter y for yes and n for no: ").strip().lower()

        
         while choice not in ['y', 'n']:
             print("Invalid choice! Please enter y or n.")
             choice = input("Enter y for yes and n for no: ").strip().lower()

         if choice == 'n': 
          print("Thanks for playing! Goodbye!")
          break



def main():
    while True:
        print("\nChoose one of the following: ")
        print("1. Calculator")
        print("2. Guessing Game")
        print("3. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            Ayesha_Imran() #function call
        elif choice == 2:
            Tahreem_Zafar()  
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main()  # Start the program
    
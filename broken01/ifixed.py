#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.
calc1 = 0.0
calc2 = 0.0
operation = ""
while calc1 != "q":
#     print("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = input("What is the first operator? Or, enter q to quit:")
    if calc1 == "Q":
        break

#     print("\nWhat is the second operator? Or, enter q to quit: ")
    calc2 = input("What is the second operator? Or, enter q to quit:")
    if calc2 == "q":
        break

    if calc1.isnumeric() == False or calc2.isnumeric() == False:
        print("Invalid input, value must be numeric!")
        break

    else:     
      calc1 = float(calc1)    
      calc2 = float(calc2)
      operation = input("Enter an operation to perform on the two operators (+ or -):")
      if operation == "+":
          print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
      elif operation == "-":
          print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
      else:
          print("\n Not a valid entry. Restarting...")

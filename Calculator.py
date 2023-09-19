print("Welcome to the Python World")
print("Here just a quick intro to the origin of Python Language:")
print("")
print("Python came from a hobby created during past Christmas time")

# print("Main menu of calculator program\n")
# print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Comparison/Boolean\n")

# choice = int(input("Please enter your choice: "))
# while True:

while True:
    print("Main menu of calculator program\n")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Comparison/Boolean\n6. Exit")

    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:
        print("Addition operation")
        inp_number = float(input("Please enter number 1: "))
        inp_number2 = float(input("Number 2 "))

        Addition = inp_number + inp_number2
        print("The result of Addition: ", Addition)

    elif choice == 2:
        print("Subtraction operation")
        inp_number = float(input("Please enter number 1: "))
        inp_number2 = float(input("Number 2: "))

        Subtraction = inp_number - inp_number2
        print("The result of subtraction: ", Subtraction)

    elif choice == 3:
        print("Multiplication operation")
        inp_number = float(input("Please enter number 1: "))
        inp_number2 = float(input("Number 2 "))

        Multiplication = inp_number * inp_number2
        print("The result of multiplication: ", Multiplication)

    elif choice == 4:
        print("Division operation")
        inp_number = float(input("Please enter number 1: "))
        inp_number2 = float(input("Number 2 "))

        Division = inp_number / inp_number2
        print("The result of division: ", Division)

    elif choice == 5:
        print("Comparison number")
        inp_number = float(input("Please enter number 1: "))
        inp_number2 = float(input("Number 2 "))

        compare = inp_number < inp_number2
        print("\nIs Number 1 < Number 2?")
        print(compare)

    else:
        break

    continue_choice = input("\nDo you want to continue? (Y/N): ")
    if continue_choice.lower() != 'y':
        break

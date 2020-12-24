import math

while True:
    print("\nChoose the math operation. \n\n0  -  Addition \n1  -  Subtraction\n2  -  Multiplication\n3  -  "
          "Division\n4  -  Modulo\n5  -  Raising to a power\n6  -  Square root\n"
          "7  -  Logarithm\n8  -  Sine\n9  -  Cosine\n10 -  Tangent\n")

    operation = input("\nYour option from the menu: ")

    # Addition

    if operation == "0":
        value1 = float(input("\nFirst Value: "))
        value2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(value1 + value2) + "\n")

        go_back = input('\nGo back to the main menu? (y/n) ')

        if go_back == 'y':
            continue
        else:
            break

        # Subtraction

    elif operation == "1":
        value1 = float(input("\nFirst Value: "))
        value2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(value1 - value2) + "\n")

        go_back = input('\nGo back to the main menu? (y/n) ')

        if go_back == 'y':
            continue
        else:
            break

        # Multiplication

    elif operation == "2":
        value1 = float(input("\nFirst Value: "))
        value2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(value1 * value2) + "\n")

        go_back = input('\nGo back to the main menu? (y/n) ')

        if go_back == 'y':
            continue
        else:
            break

        # Division

    elif operation == "3":
        value1 = float(input("\nFirst Value: "))
        value2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(value1 / value2) + "\n")

        go_back = input('\nGo back to the main menu? (y/n) ')

        if go_back == 'y':
            continue
        else:
            break

        # Modulo

    elif operation == "4":
        value1 = float(input("\nFirst Value: "))
        value2 = float(input("\nSecond Value: "))

        print("\nThe result is: " + str(value1 % value2) + "\n")

        go_back = input('\nGo back to the main menu? (y/n) ')

        if go_back == 'y':
            continue
        else:
            break

        # Raising to a power.

    elif operation == "5":
        value1 = float(input("\nEnter the base: "))
        value2 = float(input("\nEnter the power: "))

        print("\nThe result is: " + str(math.pow(value1, value2)) + "\n")

        go_back = input('\nGo back to the main menu? (y/n) ')

        if go_back == 'y':
            continue
        else:
            break

        # Square Root

    elif operation == "6":
        value1 = float(input("\nEnter value for extracting the square root: "))

        print("\nThe result is: " + str(math.sqrt(value1)) + "\n")

        go_back = input('\nGo back to the main menu? (y/n) ')

        if go_back == 'y':
            continue
        else:
            break

        # Logarithm

    elif operation == "7":
        value1 = float(input("\nEnter the value for calculating the logarithm to base 2: "))

        print("\nThe result is: " + str(math.log(value1, 2)) + "\n")

        go_back = input('\nGo back to the main menu? (y/n) ')

        if go_back == 'y':
            continue
        else:
            break

            # Sine

    elif operation == "8":
        value1 = float(input("\nEnter the value (in degrees) for calculating the sine: "))

        print("\nThe result is: " + str(math.sin(math.radians(value1))) + "\n")

        go_back = input('\nGo back to the main menu? (y/n) ')

        if go_back == 'y':
            continue
        else:
            break

        # Cosine

    elif operation == "9":
        value1 = float(input("\nEnter the value (in degrees) for calculating the cosine: "))

        print("\nThe result is: " + str(math.cos(math.radians(value1))) + "\n")

        go_back = input('\nGo back to the main menu? (y/n) ')

        if go_back == 'y':
            continue
        else:
            break

        # Tangent

    elif operation == "10":
        value1 = float(input("\nEnter the value (in degrees) for calculating the tangent: "))

        print("\nThe result is: " + str(math.tan(math.radians(value1))) + "\n")

        go_back = input('\nGo back to the main menu? (y/n) ')

        if go_back == 'y':
            continue
        else:
            break

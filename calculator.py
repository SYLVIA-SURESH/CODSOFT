def calculator():
    print("\n📱 WELCOME TO THE ADVANCED CALCULATOR")
    while True:
        print("\n🔢 Available Operations:")
        print(" + : Addition")
        print(" - : Subtraction")
        print(" * : Multiplication")
        print(" / : Division")
        print(" % : Modulus")
        print(" **: Power")
        print(" //: Floor Division")

        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")
            continue

        operation = input("Enter operation (+, -, *, /, %, **, //): ")

        try:
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            elif operation == '%':
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 % num2
            elif operation == '**':
                result = num1 ** num2
            elif operation == '//':
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 // num2
            else:
                print("❌ Invalid operation. Please try again.")
                continue

            print(f"✅ Result: {num1} {operation} {num2} = {result}")

        except ZeroDivisionError:
            print("❌ Error: Division by zero is not allowed.")

        # Ask user if they want another calculation
        again = input("\n🔁 Do you want to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("👋 Thank you for using the calculator. Goodbye!")
            break

# Run the calculator
calculator()

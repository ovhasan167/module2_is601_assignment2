from app.operations import addition, subtraction, multiplication, division

def calculator():

    print("Welcome to the Calculator! Type 'exit' to quit.")

    while True:

        user_input = input("Enter operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: ")

        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        try:
            operation, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)

        except ValueError:

            print("Invalid input. Please enter in the format: <operation> <number1> <number2>")
            continue

        if operation == 'add':
            result = addition(num1, num2)
        elif operation == 'subtract':
            result = subtraction(num1, num2)
        elif operation == 'multiply':
            result = multiplication(num1, num2)
        elif operation == 'divide':
            try:
                result = division(num1, num2)
            except ValueError as e:
                print(e)
                continue
        else:
            print("Unknown operation. Please use add, subtract, multiply, or divide.")
            continue

        print(f"The result is: {result}")
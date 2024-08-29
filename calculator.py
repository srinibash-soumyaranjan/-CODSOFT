# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Main function to run the calculator
def calculator():
    print("Welcome to the Simple Calculator!")

    # Get user inputs
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    # Perform the operation based on user's choice
    if choice == '1':
        print(f"The result of {num1} + {num2} is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result of {num1} / {num2} is: {divide(num1, num2)}")
    else:
        print("Invalid choice. Please select a valid operation.")

# Run the calculator
calculator()

# Simple Calculator Program Using Python

# Take the first number
num1 = int(input("Enter first number: "))

# Take the operator
operator = input("Enter Operator (+, -, *, /): ")

# Loop until the operator is valid
while operator in ['+', '-', '*', '/']:
    # Take the second number
    num2 = int(input("Enter second number: "))

    if operator == '+':
        num1 = num1 + num2
    elif operator == '-':
        num1 = num1 - num2
    elif operator == '*':
        num1 = num1 * num2
    elif operator == '/':
        # Check division by zero
        if num2 == 0:
            print("Error: Division by zero not allowed")
        else:
            num1 = num1 / num2

    # Print the current result
    print("Current Result is:", num1)

    # Ask for another operator
    operator = input("Enter Operator (+, -, *, /) or press any other key to exit: ")

else:
    print("You entered wrong Operator, Bye!")
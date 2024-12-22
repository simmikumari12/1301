# Function to perform addition
def addition(left, right):
    return left + right

# Function to perform subtraction
def subtraction(left, right):
    return left - right

# Function to perform multiplication
def multiplication(left, right):
    return left * right

# Function to perform division
def division(left, right):
    if right == 0:
        return "Error: Division by zero is not allowed."
    return left / right

# Function to perform modulus
def modulus(left, right):
    return left % right

# Function to perform power
def power(left, right):
    return left ** right

# Function to perform floor division
def floor_division(left, right):
    if right == 0:
        return "Error: Division by zero is not allowed."
    return left // right

#Function to process the expression and provide error if invalid expression provided
def process_expression(expression):
    parts = expression.split()
    #checking the condition if the expression provided has three parts: left operand, operator, and right operand
    if len(parts) != 3:
        return "Error: Invalid expression format. Please provide (left operand) (operator) (right operand) "
    left_str = parts[0]
    operator = parts[1]
    right_str = parts[2]

    #checking if left_str and right_str is numeric, if numeric converting in floating point ele providing an error.
    try:
        left = float(left_str)
        right = float(right_str)
    except ValueError:
        return "Eroor: Invalid Operands."

    #Checking which operand user has provided and returning the called function. If Invalid operand provinding an error.
    if operator == '+':
        return addition(left, right)
    elif operator == '-':
        return subtraction(left, right)
    elif operator == '*':
        return multiplication(left, right)
    elif operator == '/':
        return division(left, right)
    elif operator == '%':
        return modulus(left, right)
    elif operator == '**':
        return power(left, right)
    elif operator == '//':
        return floor_division(left, right)
    else:
        return "Error: Invalid operator. Please Provide: +, -, *, /, %, **, //."

#Function to take input and call the process_expression(expression)
def main():
    print("Please enter an expression:")
    while True:
        expression = input("\n")
        if expression.lower() in ('quit', 'q'):
            break
       
        result = process_expression(expression)
        print("Result:", result)


#Calling main function
main()
 
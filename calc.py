def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    if second_number == 0:
        return "Error: Cannot divide by zero."
    else:
        return first_number / second_number


while True:
    first_number = float(input("First number: "))
    operation = input("Choose +, -, *, or /: ")
    second_number = float(input("Second number: "))

    if operation == "+":
        print(add(first_number, second_number))
    elif operation == "-":
        print(subtract(first_number, second_number))
    elif operation == "*":
        print(multiply(first_number, second_number))
    elif operation == "/":
        print(divide(first_number, second_number))
    else:
        print("Please choose +, -, *, or /.")
    stop = input("Do you want to stop? (y/n): ")
    if stop.lower() == "y":
        print("Goodbye!")
        exit()  

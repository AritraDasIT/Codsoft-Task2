
def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


print("Select an operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    
    choice = input("Enter the choice(1/2/3/4): ")

    
    if choice in ('1', '2', '3', '4'):
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == '1':
            print(number1, "+", number2, "=", addition(number1, number2))

        elif choice == '2':
            print(number1, "-", number2, "=", subtraction(number1, number2))

        elif choice == '3':
            print(number1, "*", number2, "=", multiplication(number1, number2))

        elif choice == '4':
            print(number1, "/", number2, "=", division(number1, number2))
        
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
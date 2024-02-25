def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def calculator():
    print("Simple Calculator!")
    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Enter operation choice: ")
        if choice == '5':
            print("Thank You.Exiting the calculator.")
            break
        if choice in ('1','2','3','4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input.Enter numeric values.")
                continue
            if choice == '1':
                print("Result:",add(num1,num2))
            elif choice == '2':
                print("Result:",subtract(num1,num2))
            elif choice == '3':
                print("Result:",multiply(num1,num2))
            elif choice == '4':
                result = divide(num1,num2)
                if isinstance(result,str):
                    print(result)
                else:
                    print("Result:",result)
        else:
            print("Invalid input.Enter a valid choice.")

        another_calculation = input("would you like to perform another calculation?(yes/no): ").lower()
        if another_calculation!='yes':
            print("Thank You")
            break
if __name__ == "__main__":
    calculator()
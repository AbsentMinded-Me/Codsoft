# to add two numbers
def add_opr(num1, num2):
    result = num1 + num2
    print(result)

# to perform subtraction
def sub_opr(num1, num2):
    result = num1 - num2
    print(result)

# to perform multiplication
def mul_opr(num1, num2):
    result = num1 * num2
    print(result)

# to use power function
def pow_opr(num1, num2):
    result = num1 ** num2
    print(result)

# to perform division
def div_opr(num1, num2):
    try:
        result = num1 / num2
        print(result)
    except ZeroDivisionError:
        print("You cannot divide the number by zero!")

# to give options for calculator
def main():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        print("Choose the operation you want to perform:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponent")
        
        try:
            opr = int(input("Enter your choice number: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if opr == 1:
            add_opr(num1, num2)
        elif opr == 2:
            sub_opr(num1, num2)
        elif opr == 3:
            mul_opr(num1, num2)
        elif opr == 4:
            div_opr(num1, num2)
        elif opr == 5:
            pow_opr(num1, num2)
        else:
            print("Invalid Input!")

        ans = input("Do you want to continue (Y/N): ").strip().upper()
        if ans == 'Y':
            continue
        elif ans == 'N':
            break
        else:
            print("Invalid Input! Restarting the program!")

if __name__ == '__main__':
    main()

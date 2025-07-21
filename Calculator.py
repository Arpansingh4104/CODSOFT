def display_menu():
    print("\n📌 Choose an operation:")
    print("  + : Add")
    print("  - : Subtract")
    print("  * : Multiply")
    print("  / : Divide")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid number. Please try again.")

def get_operation():
    valid_ops = ['+', '-', '*', '/']
    while True:
        op = input("Enter operation (+, -, *, /): ").strip()
        if op in valid_ops:
            return op
        else:
            print("❌ Invalid operation. Choose +, -, *, or /.")

def calculate(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if n2 == 0:
            return "⚠️ Error: Division by zero is undefined."
        return n1 / n2

def main():
    print("🧮 Welcome to Simple Python Calculator")

    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        display_menu()
        operation = get_operation()

        result = calculate(num1, num2, operation)
        print(f"\n✅ Result: {num1} {operation} {num2} = {result}")

        again = input("\nWould you like to perform another calculation? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Thanks for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
    
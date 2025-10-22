from src.utils import add, subtract, multiply, divide


def display_menu():
    """Display the calculator menu."""
    print("\n=== Calculator Menu ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("=" * 23)


def get_numbers():
    """
    Get two numbers from user input.
    
    Returns:
        tuple: Two float numbers
        
    Raises:
        ValueError: If input is not a valid number
    """
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2


def calculator():
    """Main calculator function with menu-driven interface."""
    print("Welcome to the Calculator!")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '5':
                print("Thank you for using the calculator. Goodbye!")
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("Error: Invalid choice. Please select 1-5.")
                continue
            
            num1, num2 = get_numbers()
            
            if choice == '1':
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: {num1} × {num2} = {result}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    result = divide(num1, num2)
                    print(f"Result: {num1} ÷ {num2} = {result}")
        
        except ValueError as e:
            print(f"Error: Invalid input. Please enter valid numbers.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        # Ask if user wants another calculation
        continue_calc = input("\nDo another calculation? (y/n): ").strip().lower()
        if continue_calc != 'y':
            print("Thank you for using the calculator. Goodbye!")
            break


if __name__ == "__main__":
    calculator()
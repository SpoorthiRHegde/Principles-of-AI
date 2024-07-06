# Function to calculate factorial recursively
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Main function to run the factorial calculator
def main():
    print("Factorial Calculator")

    while True:
        try:
            num = int(input("Enter a non-negative integer (or -1 to exit): "))
            
            if num == -1:
                print("Exiting the factorial calculator. Goodbye!")
                break
            
            if num < 0:
                print("Please enter a non-negative integer.")
                continue

            result = factorial(num)
            print(f"The factorial of {num} is: {result}")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

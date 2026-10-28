def calculate(a, operation, b):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Error"
    else:
            return "Error"
    
    def main():
        while True:
            first_input = input("First number (or q): ")
            if first_input.strip().lower() == "q":
                break
            try:
                a = float(first_input)
                operator = input("Operator (+, -, *, /): ").strip()
                b = float(input("Second number: "))
                result = calculate(a, operator, b)
                if result == "Error":
                    print("Error")
                else:
                    print("Result:", result)
            except ValueError:
                print("Invalid input")
    
    if __name__ == "__main__":
        main()
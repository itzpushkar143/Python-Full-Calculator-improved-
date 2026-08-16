print("*** PUSHKAR'S IMPROVED CALCULATOR ***")

import operator
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '%': operator.mod,
    '**': operator.pow,
}

def get_number(prompt):
    while True:
        s = input(prompt).strip()
        if s.lower() in ('q', 'quit', 'exit'):
            return None
        try:
            return float(s)
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")

def main():
    while True:
        x = get_number("Enter the first number (or 'q' to quit): ")
        if x is None:
            break

        op = input("Enter the operator (+, -, *, /, //, %, **): ").strip()
        if op.lower() in ('q', 'quit', 'exit'):
            break
        if op not in ops:
            print("Invalid operator. Try again.")
            continue

        y = get_number("Enter the second number (or 'q' to quit): ")
        if y is None:
            break

        try:
            result = ops[op](x, y)
        except ZeroDivisionError:
            print("Error: division by zero.")
            continue

        # Print integer if it's a whole number, otherwise print float
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        print(f"Answer: {result}")

        again = input("Do you want to run again? (yes/no) : ").strip().lower()
        if again not in ('yes', 'y'):
            break

    print("Thanks for using the calculator.")

if __name__ == "__main__":
    main()

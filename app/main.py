"""CLI entry point — lets students interact with the calculator locally."""

import sys
from app.calculator import add, subtract, multiply, divide

OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


def main():
    if len(sys.argv) != 4:
        print("Usage: python -m app.main <operation> <num1> <num2>")
        print(f"Operations: {', '.join(OPERATIONS)}")
        sys.exit(1)

    op, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])

    if op not in OPERATIONS:
        print(f"Unknown operation: {op}")
        sys.exit(1)

    result = OPERATIONS[op](a, b)
    print(f"{a} {op} {b} = {result}")


if __name__ == "__main__":
    main()

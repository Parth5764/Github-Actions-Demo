# main.py

import argparse

def add(a, b):
    return a + b

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument("a", type=int, help="First number")
    parser.add_argument("b", type=int, help="Second number")
    args = parser.parse_args()

    result = add(args.a, args.b)
    print(f"The result is {result}")

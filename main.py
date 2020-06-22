#!/home/joaofortunato/.virtualenvs/calculator/bin/python3.6

def main():
    """Receives an arithmetic expression, parses, evaluates & shows result."""
    print("Arithmetic Calculator\n")
    print("Supported Symbols:")
    print("   - negative and positive number;")
    print("   - +, -, /, * and parentheses.\n")

    expression = input("Insert expression (insert exit to quit the app)>>>")

    while expression != "exit":

        expression = input("Insert expression (\"exit\" to quit the app)>>>")


if __name__ == "__main__":
    main()

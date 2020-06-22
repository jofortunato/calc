#!/home/joaofortunato/.virtualenvs/calculator/bin/python3.6

def parse_expression(expression):
    """Receive math expression and returns list of items.

    Each item is an element of the expression.
    Example: input: "1+2*2" >> output: ["1","+","2","*","2"]
    """
    parsed_expression = []

    for character in expression:
        if character.isdigit():
            if parsed_expression[-1].isdigit():
                parsed_expression[-1] += character
            else:
                parse_expression.append(character)
        elif character in "-+*/()":
            parse_expression.append(character)

    return parsed_expression


def calculator(expression):
    parsed_exp = parse_expression(expression)

    return result

def main():
    """Receives an arithmetic expression, parses, evaluates & shows result."""
    print("Arithmetic Calculator\n")
    print("Supported Symbols:")
    print("   - negative and positive number;")
    print("   - +, -, /, * and parentheses.\n")

    expression = input("Insert expression (insert exit to quit the app)>>>")

    while expression != "exit":

        expression = input("Insert expression (\"exit\" to quit the app)>>>")
        result = calculator(expression)

        print("Result:"+result)


if __name__ == "__main__":
    main()

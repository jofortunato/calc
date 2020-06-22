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


def infix2postfix(infix_expression):
    """Infix notation to Postfix notation.

    Receive a list of math expression elements in infix notation and
    convert to postfix notation using The Shunting Yard Algorithm.
    Example: input: ["2","+","1","*","3"] >> output ["2","1","3","*","+"]
    """
    postfix_expression = []
    operators = []
    high_precedence = "*/"
    low_precedence = "+-"

    for element in infix_expression:
        if element.isnumeric():
            postfix_expression.append(element)
        elif element == "(":
            operators.append(element)
        elif element == ")":
            while operators[-1] != "(":
                postfix_expression.append(operators[-1])
                operators.pop()
            operators.pop()
        elif element in "+-/*":
            if not operators or operators[-1] == "(":
                operators.append(element)
            elif element in high_precedence and\
                    operators[-1] is low_precedence:
                operators.append(element)
            while element in high_precedence or\
                    (element is low_precedence and
                     operators[-1] is high_precedence):
                postfix_expression.append(operators[-1])
                operators.pop()

    while operators:
        if operators[-1] in "()":
            operators.pop()
        postfix_expression.append(operators[-1])
        operators.pop()

    return postfix_expression


def calculator(expression):

    expression_list = parse_expression(expression)

    postfix_expression = infix2postfix(expression_list)

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

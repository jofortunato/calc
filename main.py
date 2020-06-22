#!/home/joaofortunato/.virtualenvs/calculator/bin/python3.6

def parse_expression(expression):
    """Receive math expression and returns list of items.

    Each item is an element of the expression.
    Example: input: "1+2*2" >> output: ["1","+","2","*","2"]
    """
    parsed_expression = [""]

    for character in expression:
        if character.isdigit():
            if parsed_expression[-1].isdigit():
                parsed_expression[-1] += character
            else:
                parsed_expression.append(character)
        elif character in "-+*/()":
            parsed_expression.append(character)

    parsed_expression.pop(0)

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
            while operators and operators[-1] != "(":
                postfix_expression.append(operators[-1])
                operators.pop()
            operators.pop()
        elif element in "+-/*":
            if (not operators) or operators[-1] == "(":
                operators.append(element)
            elif element in high_precedence and\
                    operators[-1] in low_precedence:
                operators.append(element)
            else:
                while operators and (element in high_precedence or
                                     (element in low_precedence and
                                      operators[-1] in low_precedence)):
                    postfix_expression.append(operators[-1])
                    operators.pop()
                operators.append(element)

    while operators:
        if operators[-1] in "()":
            operators.pop()
        postfix_expression.append(operators[-1])
        operators.pop()

    return postfix_expression


def simple_calculation(num1, num2, operator):
    """Perform simple calculation: num1 and num2 using specific operator."""
    if operator == "+":
        return str(float(num1) + float(num2))
    elif operator == "-":
        return str(float(num1) - float(num2))
    elif operator == "*":
        return str(float(num1) * float(num2))
    elif operator == "/":
        return str(float(num1) / float(num2))


def calculator(expression):
    """Calculate result of a postfix math expression."""
    inflix_expression = parse_expression(expression)
    print(inflix_expression)
    postfix_expression = infix2postfix(inflix_expression)
    print(postfix_expression)

    temp_result = []

    for element in postfix_expression:
        if element in "+-/*":
            temp = simple_calculation(temp_result[-2],
                                      temp_result[-1],
                                      element)
            temp_result.pop()
            temp_result.pop()
            temp_result.append(temp)
        else:
            temp_result.append(element)

    return temp_result[0]


def main():
    """Receives an arithmetic expression, parses, evaluates & shows result."""
    print("Arithmetic Calculator\n")
    print("Supported Symbols:")
    print("   - negative and positive number;")
    print("   - +, -, /, * and parentheses.\n")

    expression = str(input("Insert expression (\"exit\" to quit the app)>>>"))

    while expression != "exit":
        result = calculator(expression)
        print("Result: "+result+"\n")
        expression = str(input("Insert expression (\"exit\" to quit the app)>>>"))


if __name__ == "__main__":
    main()

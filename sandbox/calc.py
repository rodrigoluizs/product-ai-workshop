"""A tiny calculator you can read top to bottom.

It takes a line of text like "1 + 2 * 3" and prints the answer.

What it supports today:
  - the four operators:  +  -  *  /
  - whole numbers and decimals (like 1.5)
  - normal math order: multiply and divide happen BEFORE add and subtract,
    so "1 + 2 * 3" is 7, not 9.

What it does NOT support yet:
  - parentheses, like "(1 + 2) * 3"   <-- this is the feature we plan in the workshop

The code has three small steps: tokenize -> evaluate -> print.
"""


def tokenize(text):
    """Turn a line of text into a list of numbers and operators.

    Example:  "1 + 2*3"  ->  [1.0, "+", 2.0, "*", 3.0]
    """
    tokens = []
    number = ""  # we collect the digits of a number here, one character at a time

    for char in text:
        if char in "0123456789.":
            number += char
        elif char in "+-*/":
            if number != "":
                tokens.append(float(number))
                number = ""
            tokens.append(char)
        elif char == " ":
            if number != "":
                tokens.append(float(number))
                number = ""
        else:
            raise ValueError("I don't understand this character: " + repr(char))

    if number != "":
        tokens.append(float(number))

    return tokens


def apply(operator, left, right):
    """Do the actual arithmetic for one operator."""
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return left / right
    raise ValueError("Unknown operator: " + repr(operator))


def collapse(tokens, operators):
    """Go left to right; whenever we see one of `operators`, combine the number
    before it and the number after it into a single number.

    This is how we do "multiply/divide first": we collapse * and / in one pass,
    then collapse + and - in a second pass.
    """
    result = [tokens[0]]
    index = 1
    while index < len(tokens):
        operator = tokens[index]
        right = tokens[index + 1]
        if operator in operators:
            left = result.pop()
            result.append(apply(operator, left, right))
        else:
            result.append(operator)
            result.append(right)
        index += 2
    return result


def evaluate(tokens):
    """Reduce a list of tokens down to one number."""
    tokens = collapse(tokens, ["*", "/"])  # first pass: × and ÷
    tokens = collapse(tokens, ["+", "-"])  # second pass: + and −
    return tokens[0]


def calculate(text):
    """The whole pipeline: text in, number out."""
    return evaluate(tokenize(text))


def format_result(value):
    """Show 4 instead of 4.0, but keep 3.5 as 3.5."""
    if value == int(value):
        return str(int(value))
    return str(value)


def main():
    """The interactive prompt. Type an expression and press Enter."""
    print("calc — type an expression, or 'quit' to exit")
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        if line.strip() in ("quit", "exit"):
            break
        if line.strip() == "":
            continue
        try:
            print(format_result(calculate(line)))
        except (ValueError, ZeroDivisionError) as error:
            print("error: " + str(error))


if __name__ == "__main__":
    main()

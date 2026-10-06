# Perform the mathematical operation specified by the operator.

def basic_op(operator, value1, value2):

    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2
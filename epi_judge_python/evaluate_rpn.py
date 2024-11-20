from test_framework import generic_test
from typing import List 

def evaluate(expression: str) -> int:
    delimiter = ","
    symbols = expression.split(delimiter)
    stack: List[int] = []

    for token in symbols:
        if token in "-+*/":
            operator = token 
            first_expression = stack.pop()
            second_expression = stack.pop()

            match operator:
                case "-":
                    new_expression = second_expression - first_expression
                case "+":
                    new_expression = second_expression + first_expression
                case "*":
                    new_expression = second_expression * first_expression
                case "/":
                    new_expression = second_expression // first_expression
                case _:
                    print(f"Malformed RPN at {operator}")
            
            stack.append(new_expression)
        else:
            stack.append(int(token))
    
    return stack[-1]




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))

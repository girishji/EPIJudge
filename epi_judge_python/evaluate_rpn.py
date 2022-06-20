from test_framework import generic_test


def evaluate(expression: str) -> int:
    stack = []
    op = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: y - x,
        "*": lambda x, y: x * y,
        "/": lambda x, y: y // x,
    }
    for x in expression.split(","):
        if x in op.keys():
            stack.append(op[x](stack.pop(), stack.pop()))
        else:
            # if x == '+':
            #     stack.append(stack.pop() + stack.pop())
            # elif x == '-':
            #     stack.append(-stack.pop() + stack.pop())
            # elif x == '*':
            #     stack.append(stack.pop() * stack.pop())
            # elif x == '/':
            #     op = stack.pop()
            #     stack.append(stack.pop() // op)
            # else:
            stack.append(int(x))

    return stack.pop()


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", "evaluate_rpn.tsv", evaluate)
    )

from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    stack = []
    matching = {'}' : '{', ']' : '[', ')' : '('}
    for x in s:
        if x in matching.keys():
            if len(stack) > 0 and stack[-1] == matching[x]:
                stack.pop()
            else:
                return False
        else:
            stack.append(x)
    return True if len(stack) == 0 else False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))

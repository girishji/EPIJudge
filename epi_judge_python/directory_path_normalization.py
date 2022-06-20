from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    if len(path) == 1 and path == '.':
        return path
    root = True if path and path[0] == '/' else False
    stack = []
    for x in path.split('/'):
        if x == '..':
            if len(stack) > 0 and stack[-1] != '..':
                stack.pop()
            else:
                stack.append(x)
        elif x and x != '.':
            stack.append(x)
    return ('/' if root else '') + '/'.join(stack)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))

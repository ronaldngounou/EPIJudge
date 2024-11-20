from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    if not path:
        raise ValueError("Empty string is not a valid path.")
    
    path_names = [] # Uses list as a stack.

    # Special case: starts with '/' which is an absolute path
    if path[0] == '/':
        path_names.append('/')

    for token in path.split('/'):
        if token in [".", ""]:
            continue
        if token == "..":
            if not path_names or path_names[-1] == '..':
                path_names.append(token)
            else:
                if path_names[-1] == '/':
                    raise  ValueError("Trying to go up root")
                path_names.pop()
        else:
            path_names.append(token)
    
    result = '/'.join(path_names)
    return result[result.startswith('//'):]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))

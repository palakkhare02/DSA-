def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    """
    result = []

    # Upper part
    for i in range(n, 0, -1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        result.append(spaces + stars)

    # Lower part (skip middle row because already included)
    for i in range(2, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        result.append(spaces + stars)

    return result

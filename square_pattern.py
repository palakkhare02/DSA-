# Square of side 'N'

def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    square = []
    
    # Loop n times to generate each row
    for i in range(n):
        square.append('*' * n)
    
    return square

# Take input from user
n = int(input("Enter the size of the square: "))

# Print the resulting square pattern
result = generate_square(n)
print(result)

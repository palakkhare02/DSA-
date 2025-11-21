def celsius_to_fahrenheit(C):
    """
    Function to convert temperature from Celsius to Fahrenheit.
    
    Parameters:
    C (float): The temperature in Celsius.
    
    Returns:
    float: The temperature in Fahrenheit.
    """
    # Your code here
    F = (9/5 * C) + 32
    return F

def area_of_rectangle(length, breadth):
    """
    Function to calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    breadth (float): The breadth of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    # Your code here
    area =length*breadth
    return area


def calculate_distance(speed, time):
    """
    Function to calculate the distance traveled by a vehicle.
    
    Parameters:
    speed (float): The speed of the vehicle.
    time (float): The time the vehicle has traveled.
    
    Returns:
    float: The distance traveled by the vehicle.
    """
    # Your code here
    Distance=speed*time
    return Distance
    
def calculate_lift_rounds(n, capacity):
    """
    Function to calculate the number of rounds the lift needs to cover.
    
    Parameters:
    n (int): Total number of people.
    capacity (int): Maximum number of people the lift can carry in one round.
    
    Returns:
    int: The number of rounds required to transport all people to the top floor.
    """
    # Your code here
    rounds = (n + capacity - 1) // capacity
    return rounds


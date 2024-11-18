"""Math exercises."""
import math

def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    
    sum_result = num_a + num_b
    difference_result = num_a - num_b
    return sum_result, difference_result


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    
    division_result = num_a / num_b
    return division_result


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    
    division_result = num_a // num_b
    return division_result


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    
    product = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return product, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    
    average = (num_a + num_b) / 2
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    
    pi = 3.14159
    area = pi * radius ** 2
    return round(area, 2)


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    
    if side_length == 0:
        return 0
    sqrt_3 = 3 ** 0.5
    area = (sqrt_3 / 4) * side_length ** 2
    return round(area, 0)


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    
    discriminant = b**2 - 4 * a * c
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    
    c = math.sqrt(a**2 + b**2)
    return c


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    
    b = math.sqrt(c**2 - a**2)
    return b
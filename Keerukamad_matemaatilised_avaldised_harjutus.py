"""Math exercises vol2."""
import math

def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."


def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    
    radians = math.radians(angle)
    sine = math.sin(radians)
    cosine = math.cos(radians)
    return f"Nurk: {angle}, siinus: {sine:.1f}, koosinus: {cosine:.1f}."


def greetings(n: int) -> str:
    """Return a string that contains "Hey" n times."""
    return "Hey" * n


def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string."""
    
    result = num_a + num_b
    return str(result)
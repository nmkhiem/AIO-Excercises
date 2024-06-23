import math

def is_integer(n):
    try:
        int(n) # Type - casting the string to 'int',
                  # If string is not a valid 'int',
                  # it'll raise 'ValueError' exception
    except ValueError:
        return False
    return True

def is_float(n):
    try:
        int(n) # Type - casting the string to 'float',
                  # If string is not a valid 'float',
                  # it'll raise 'ValueError' exception
    except ValueError:
        return False
    return True

def approx_sin(x, n):
    """
    Approximates the sine function using a Taylor series expansion.

    Inputs:
        x (float): Input value (in radians).
        n (int): Number of terms in the series.

    Output:
        sin (float): Approximated sine value.
    """
    if is_integer(n) and is_float(x):
        sin = 0
        for i in range(n):
            sin += ((-1) ** i) * (x ** (2*i + 1)) / math.factorial(2*i +1)
        return sin

def approx_cos(x, n):
    """
    Approximates the cosine function using a Taylor series expansion.

    Inputs:
        x (float): Input value (in radians).
        n (int): Number of terms in the series.

    Output:
        cos (float): Approximated cosine value.
    """
    if is_integer(n) and is_float(x):
        cos = 0
        for i in range(n):
            cos += ((-1) ** i) * (x ** (2*i)) / math.factorial(2*i)
        return cos
    
def approx_sinh(x, n):
    """
    Approximates the sinh function using a Taylor series expansion.

    Inputs:
        x (float): Input value (in radians).
        n (int): Number of terms in the series.

    Output:
        sinh (float): Approximated sinh value.
    """
    if is_integer(n) and is_float(x):
        sinh = 0
        for i in range(n):
            sinh += (x ** (2*i + 1)) / math.factorial(2*i +1)
        return sinh

def approx_cosh(x, n):
    """
    Approximates the cosh function using a Taylor series expansion.

    Inputs:
        x (float): Input value (in radians).
        n (int): Number of terms in the series.

    Output:
        cosh (float): Approximated cosh value.
    """
    if is_integer(n) and is_float(x):
        cosh = 0
        for i in range(n):
            cosh += (x ** (2*i)) / math.factorial(2*i)
        return cosh
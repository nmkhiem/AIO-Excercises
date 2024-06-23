import numpy as np

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

def md_nre(y, y_hat, n = 2, p = 1):
    '''
    Calculates the Mean Difference of normalized Relative Errors (MD_nRE).

    Inputs:
        y (float): True values.
        y_hat (float): Predicted values.
        n (int, optional): Degree of normalization (default is 2).
        p (int, optional): Power for the difference (default is 1).

    Output:
        float: MD_nRE value.
    '''
    if is_float(y) and is_float(y_hat) and is_integer(n) and is_integer(p):
        MD_nRE = np.mean((y ** (1/n) - y_hat ** (1/n)) ** p) 
        return MD_nRE
    else:
        print('The input type is incorrect!')
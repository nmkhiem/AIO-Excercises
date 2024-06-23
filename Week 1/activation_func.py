import math


def is_number(n):
    try:
        float(n)  # Type - casting the string to 'float',
        # If string is not a valid 'float',
        # it'll raise 'ValueError' exception
    except ValueError:
        return False
    return True


def count_activation():
    '''
    Calculates activation values for different functions (sigmoid, relu, elu).

    Args:
        None

    Returns:
        float: Activation value based on user input.
    '''
    x = input('Input x: ')
    activation_name = input(
        'Input activation name  (sigmoid | relu | elu): ').lower()

    if is_number(x):
        x = float(x)
        if activation_name == 'sigmoid':
            sigmoid = 1 / (1 + math.exp(-x))
            print(f'Sigmoid: f({x}) = {sigmoid}')
            return sigmoid
        elif activation_name == 'relu':
            if x < 0:
                print(f'Relu: f({0}) = {0}')
                return 0
            else:
                print(f'Relu: f({x}) = {x}')
                return x
        elif activation_name == 'elu':
            if x < 0:
                alpha = input('Input alpha: ')
                if is_number(alpha):
                    alpha = float(alpha)
                else:
                    print('alpha must be a number')
                    return
                elu = alpha * (math.exp(x) - 1)
                print(f'Elu: f({x}) = {elu}')
            else:
                print(f'Elu: f({x}) = {x}')
                return x
        else:
            print(f'There is no activation function named {activation_name}')
    else:
        print('x must be a number')

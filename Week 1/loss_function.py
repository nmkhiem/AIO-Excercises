import numpy as np
def is_integer(n):
    try:
        int(n) # Type - casting the string to 'int',
                  # If string is not a valid 'int',
                  # it'll raise 'ValueError' exception
    except ValueError:
        return False
    return True

def MAE(pred, target):
    '''
    Calculates the Mean Absolute Error (MAE) between predicted and target values.

    Inputs:
        pred (float): Predicted values.
        target (float): True target values.

    Output:
        mae (float): MAE values.
    '''
    mae = np.mean(np.abs(pred - target))
    return mae

def MSE(pred, target):
    '''
    Calculates the Mean Squared Error (MSE) between predicted and target values.

    Inputs:
        pred (float): Predicted values.
        target (float): True target values.

    Output:
        mse (float): MSE values.
    '''
    mse = np.mean(((pred - target)**2))
    return mse

def RMSE(pred, target):
    '''
    Calculates the Root Mean Squared Error (RMSE) between predicted and target values.

    Inputs:
        pred (float): Predicted values.
        target (float): True target values.

    Output:
        rmse (float): RMSE values.
    '''
    rmse = np.mean(((pred - target)**2)) ** (1/2)
    return rmse

def loss():
    '''
    Calculates various loss functions for randomly generated samples.

    Input:
        None

    Output:
        None: Print loss values.
    '''
    num_samples = input('Input number of samples: ')
    loss_name = input('Input number loss name (MSE | MAE | RMSE): ').lower()
    if is_integer(num_samples):
        num_samples = int(num_samples)
        for i in range(num_samples):
            pred = np.random.rand(1)[0]
            target = np.random.rand(1)[0]
            if loss_name == 'mse':
                mse = MSE(pred, target)
                print(f'Loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}')
                print('Loss: ', mse)
            elif loss_name == 'mae':
                mae = MAE(pred, target)
                print(f'Loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}')
                print('Loss: ', mae)
            elif loss_name == 'rmse':
                rmse = RMSE(pred, target)
                print(f'Loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}')
                print('Loss: ', rmse)
            else:
                print(f'Loss function named {loss_name} is not supported')
                return
    else:
        print('x must be an integer')
        return 



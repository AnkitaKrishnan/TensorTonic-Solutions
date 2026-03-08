import numpy as np


def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x)
    ans = 1/( 1 + np.exp(-x) )
    return ans
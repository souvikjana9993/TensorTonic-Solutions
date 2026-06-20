import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    prob = np.array(p)
    if np.sum(prob) != 1:
       raise ValueError
    else:
        return np.sum(np.multiply(np.array(x),np.array(p)))
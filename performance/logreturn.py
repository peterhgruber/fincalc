# fincalc/performance/logreturn.py

import numpy as np
import pandas as pd

def logreturn(price):
    """
    Calculate the time series of log returns.
    
    Parameters:
    - prices: A pandas series.
    
    Returns:
    - The log returns.
    """
    
    return np.log(price) - np.log(price.shift(1))
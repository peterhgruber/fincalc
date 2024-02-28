# fincalc/performance/simplereturn.py

import numpy as np
import pandas as pd

def simplereturn(price):
    """
    Calculate the time series of simple returns.
    
    Parameters:
    - price: A pandas series.
    
    Returns:
    - The simple returns.
    """
    
    return  price.pct_change()
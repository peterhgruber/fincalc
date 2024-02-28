# FinanceCalc/PV/continuous.py

import numpy as np

def continuous(future_value, rate, time):
    """
    Calculate the present value of a future sum of money using continuous compounding interest.
    
    Parameters:
    - future_value: The future value of the money.
    - rate: The annual interest rate (as a decimal).
    - time: The time in years until the future value is realized.
    
    Returns:
    - The present value of the future sum of money.
    """
    return future_value / np.exp(rate * time)

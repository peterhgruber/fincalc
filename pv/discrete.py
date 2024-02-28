# FinanceCalc/PV/discrete.py

def discrete(future_value, rate, time):
    """
    Calculate the present value of a future sum of money using discrete compounding interest.
    
    Parameters:
    - future_value: The future value of the money.
    - rate: The annual interest rate (as a decimal).
    - time: The time in years until the future value is realized.
    
    Returns:
    - The present value of the future sum of money.
    """
    
    return future_value / (1 + rate) ** time

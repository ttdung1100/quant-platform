import numpy as np

def sharpe_ratio(returns):

    mean = returns.mean()
    std = returns.std()

    return mean / std
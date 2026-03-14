def volatility(returns):

    return returns.std()

def drawdown(price):

    cummax = price.cummax()

    dd = (price - cummax) / cummax

    return dd
def moving_average_strategy(price):

    ma50 = price.rolling(50).mean()
    ma200 = price.rolling(200).mean()

    signal = ma50 > ma200

    return signal
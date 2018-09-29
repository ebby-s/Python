def root(num,accuracy):
    sqrt = 1
    while sqrt**2 - num > 10**-accuracy or num - sqrt**2 > 10**-accuracy:
        sqrt = (sqrt + num/sqrt)/2
    return round(sqrt,accuracy)

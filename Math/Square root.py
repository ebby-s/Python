def root(num,acc):
    sqrt = 1
    while sqrt**2 - num > 10**-acc or num - sqrt**2 > 10**-acc:
        sqrt = (sqrt + num/sqrt)/2
    return round(sqrt,acc)

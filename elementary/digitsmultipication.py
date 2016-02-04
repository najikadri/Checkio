def checkio(number):
    numb = str(number)
    mult = []
    res = 1
    for i in numb:
            mult.append(int(i))
    for x in mult:
        if x > 0:
            res *= x
    return res

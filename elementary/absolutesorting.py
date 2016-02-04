import operator

def checkio(numbers_array):
    a = numbers_array
    b = [abs(x) for x in a]
    c = dict()
    
    for x in range(len(a)):
        c[a[x]] = b[x]
    return [x[0] for x in sorted(c.items(), key=operator.itemgetter(1))]

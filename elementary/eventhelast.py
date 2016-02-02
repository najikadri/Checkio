def checkio(array):
    e = []
    for x in range(len(array)):
        if x % 2 == 0:
            e.append(array[x])
    return (sum(e)*array[-1] if len(e) > 0 else 0)

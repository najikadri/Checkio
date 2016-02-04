def checkio(data):
    dat = data
    for x in dat:
        if dat.count(x) == 1:
            dat.remove(x)
    return dat

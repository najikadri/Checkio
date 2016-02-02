def checkio(words):
    m = c = 0
    w = words.split()
    for x in range(len(w)):
        if not w[x].isnumeric():
            c += 1
            m = (c if c > m else m)
        else:
            c = 0
    return (True if m >= 3 else False)

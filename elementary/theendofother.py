def checkio(words_set):
    for x in words_set:
        a = [y for y in words_set if y is not x]
        for z in a:
            w = z[len(z)-len(x):len(z)]
            if w == x:
                return True
    return False

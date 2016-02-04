def checkio(first, second):
    first = first.split(',')
    second = second.split(',')
    words = []
    res = ''
    for x in first:
        if x in second:
            words.append(x)
    for y in sorted(words):
        res += (','+y if y != sorted(words)[0] else y)
    return res

def checkio(*args):
    e = []
    for i in range(len(args)):
     e.append(args[i])
    return (max(e)-min(e) if len(e) > 0 else 0)

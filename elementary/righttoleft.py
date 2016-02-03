def left_join(phrases):
    str = ''
    for i in range(len(phrases)):
        str = str +  (","+phrases[i] if i > 0 else phrases[i])
        
    str = str.replace('right','left')
    return str

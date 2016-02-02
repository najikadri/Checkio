def find_message(text):
    word = ''
    for l in text:
        if l.isupper():
            word = word+l
    return word

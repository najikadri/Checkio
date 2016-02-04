def check_pangram(text):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    text = text.lower()
    for l in alpha:
        if l in text:
            count += 1
    return (True if count is len(alpha) else False)

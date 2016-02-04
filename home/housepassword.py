def checkio(data):
    if  any(char.isdigit() for char in data)and any(char.isalpha() for char in data)and any(char.isupper() for char in data)and any(char.islower() for char in data) and len(data)>= 10 :
        return True
    return False

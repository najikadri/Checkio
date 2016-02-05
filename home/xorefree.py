def checkio(game_result):
    x = ver(game_result,'X') or hor(game_result,'X') or cur(game_result,'X')
    o = ver(game_result,'O') or hor(game_result,'O') or cur(game_result,'O')
    if x and not o:
        return 'X'
    elif o and not x:
        return 'O'
    else:
        return 'D'

def hor (game,value):
    for x in game:
        if x[0] == x[1] == x[2] == value:
            return True
    return False

def ver (game,value):
    for i in range(len(game)):
        if game[0][i] == game[1][i] == game[2][i] == value:
            return True
    return False

def cur (game,value):
    if game[0][0] == game[1][1] == game[2][2] == value:
        return True
    elif game[0][2] == game[1][1] == game[2][0] == value:
        return True
    return False

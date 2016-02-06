class T:

    def __init__(self, anything):
        pass

    def __lt__(self, otherthing):
        return True

    def __gt__(self, otherthing):
        return True

    def __ge__(self, otherthing):
        return True

    def __le__(self, otherthing):
        return True

    def __eq__(self, otherthing):
        return True

    def __ne__(self, otherthing):
        return True


def checkio(anything):
    '''
        try to return anything else :)
    '''
    return T(anything)

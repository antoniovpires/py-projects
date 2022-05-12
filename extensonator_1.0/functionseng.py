def unidade(number):
    if number == 0:
        return('zero')
    elif number == 1:
        return('one')
    elif number == 2:
        return('two')
    elif number == 3:
        return('three')
    elif number == 4:
        return('four')
    elif number == 5:
        return('five')
    elif number == 6:
        return('six')
    elif number == 7:
        return('seven')
    elif number == 8:
        return('eight')
    elif number == 9:
        return('nine')
    elif number == 10:
        return('ten')
    elif number == 11:
        return('eleven')
    elif number == 12:
        return('twelve')
    elif number == 13:
        return('thirteen')
    elif number == 14:
        return('fourteen')
    elif number == 15:
        return('fifteen')
    elif number == 16:
        return('sixteen')
    elif number == 17:
        return('seventeen')
    elif number == 18:
        return('eighteen')
    elif number == 19:
        return('nineteen')

def dezena(number):
    if number == 2:
        return ('twenty')
    elif number == 3:
        return ('thirty')
    elif number == 4:
        return ('forty')
    elif number == 5:
        return ('fifty')
    elif 10 > number >= 6:
        if str(unidade(number))[-1] == 't':
            return f'{unidade(number)}'+'y'
        else:
            return f'{unidade(number)}'+'ty'

def centena(number):
    return f'{unidade(number)} hundred'

def milhar(number):
    return f'{unidade(number)} thousand'

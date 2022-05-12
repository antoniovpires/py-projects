import functionsptbr
import functionseng

language = int(input(f'Which language do you want to use? \n [1] English\n [2] Brazilian Portuguese\n '
                     f'{"="*len("[2] Brazilian Portuguese")}'
                     f'\n'))
if language == 2:
    num = int(input('Digite um número de [0] à [999]: '))
    if num <= 19:
        print(functionsptbr.unidade(num))
    elif 20 <= num < 99:
        if int(str(num)[1]) > 0:
            print(f'{functionsptbr.dezena(int(str(num)[0]))} e {functionsptbr.unidade(int(str(num)[1]))}')
        else:
            print(f'{functionsptbr.dezena(int(str(num)[0]))}')
    elif num == 100:
        print('cem')
    elif num > 100:
        if int(str(num)[1]) == 0:
            print(f'{functionsptbr.centena(int(str(num)[0]))} e {functionsptbr.unidade(int(str(num)[2]))}')
        elif int(str(num)[2]) == 0:
            print(f'{functionsptbr.centena(int(str(num)[0]))} e {functionsptbr.dezena(int(str(num)[1]))}')
        elif int(str(num)[1:]) < 20:
            print(f'{functionsptbr.centena(int(str(num)[0]))} e {functionsptbr.unidade(int(str(num)[1:]))}')
        else:
            print(f'{functionsptbr.centena(int(str(num)[0]))} e '
                  f'{functionsptbr.dezena(int(str(num)[1]))} e '
                  f'{functionsptbr.unidade(int(str(num)[2]))}')

    print('Pronto!')
elif language == 1:
    num = int(input('Insert a number from [0] to [9999]: '))
    if num <= 19:
        print(functionseng.unidade(num))
    elif 20 <= num < 99:
        if int(str(num)[1]) > 0:
            print(f'{functionseng.dezena(int(str(num)[0]))} {functionseng.unidade(int(str(num)[1]))}')
        else:
            print(f'{functionseng.dezena(int(str(num)[0]))}')
    elif 999 >= num >= 100:
        if int(str(num)[1]) == 0:
            print(f'{functionseng.centena(int(str(num)[0]))} and {functionseng.unidade(int(str(num)[2]))}')
        elif int(str(num)[2]) ==0:
            print(f'{functionseng.centena(int(str(num)[0]))} {functionseng.dezena(int(str(num)[1]))}')
        elif int(str(num)[1:]) < 20:
            print(f'{functionseng.centena(int(str(num)[0]))} and {functionseng.unidade(int(str(num)[1:]))}')
        else:
            print(f'{functionseng.centena(int(str(num)[0]))} '
                  f'{functionseng.dezena(int(str(num)[1]))} '
                  f'{functionseng.unidade(int(str(num)[2]))}')
    elif num > 999:
        if int(str(num)[1]) == 0:
            if int(str(num)[2:]) < 20:
                print(f'{functionseng.milhar(int(str(num)[0]))} and {functionseng.unidade(int(str(num)[1:]))}')
            else:
                print(f'{functionseng.milhar(int(str(num)[0]))} and {functionseng.dezena(int(str(num)[2]))} '
                      f'{functionseng.unidade(int(str(num)[3]))}')
        elif int(str(num)[3]) ==0:
            print(f'{functionseng.milhar(int(str(num)[0]))} {functionseng.centena(int(str(num)[1]))} '
                  f'{functionseng.dezena(int(str(num)[2]))}')
        else:
            print(f'{functionseng.milhar(int(str(num)[0]))} '
                  f'{functionseng.centena(int(str(num)[1]))} '
                  f'{functionseng.dezena(int(str(num)[2]))} '
                  f'{functionseng.unidade(int(str(num)[3]))}')
    print('Done!')
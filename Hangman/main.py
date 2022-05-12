from forca import forca


print('-=-'*8)
palavra = input('Digite uma palavra: ').lower()
clone = list('_' for l in palavra)
print('-=-'*8)
print(' '.join(clone))
cont = 0
palavras_erradas = []
while True:
    print('-=-'*8)
    palpite = input('Digite uma letra: ').lower()
    if palpite not in palavra:
        palavras_erradas.append(palpite)
        print('Errou!')
        cont +=1
        forca(cont)
        print(f"Palpites errados = {' '.join(palavras_erradas)}")
    if cont == 6:
        print('Você perdeu!')
        break
    for l in range(0, len(palavra)):
        if palavra[l] == palpite:
            clone[l] = palpite
    print('-=' * 20)
    print(' '.join(clone))
    if '_' not in clone:
        print('Parabéns! Você venceu ;D')
        break

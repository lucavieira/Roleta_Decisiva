from random import randint


def decida(quantidade_opcoes):
    opcoes = list()
    titulo = str(input('Qual será o titulo da Roleta: ')).title()
    for valor in range(1, quantidade_opcoes+1):
        opcao = str(input(f'{valor}° Opção: ')).capitalize()
        while opcao in opcoes:
            print('\033[31mEstá opção já foi adicionada, informe uma outra opção.\033[m')
            opcao = str(input(f'{valor}° Opção: ')).capitalize()
        opcoes.append(opcao)

    while True:
        try:
            quantidade_resultados = int(input('Quantos resultados deseja: '))
        except ValueError:
            print('\033[31mERROR: Digite apenas valores inteiros\033[m')
        else:
            print('-' * 35)
            print(f'{titulo.center(35)}')
            print('-' * 35)
            print('Os resultados são:')
            for valor in range(1, quantidade_resultados+1):
                index = randint(0, len(opcoes) - 1)
                print(opcoes[index])
            break


while True:
    try:
        a = int(input('Quantas opcoes: '))
    except ValueError:
        print('\033[31mERROR: Digite apenas valores inteiros\033[m')
    else:
        decida(a)
        break

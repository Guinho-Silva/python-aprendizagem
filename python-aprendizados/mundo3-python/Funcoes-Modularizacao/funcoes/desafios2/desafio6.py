'''6)Faça um mini-sistema que utilize o interactive help do python. O usuário vai digitar e o comando manual vai aparecer. Quandoo o usuário digitar a palavra "FIM", o programa se encerrará

obs: use cores'''




def ajuda():
    """
    Mini-sistema de ajuda interativa do Python.
    O usuário digita o nome de um comando, função ou módulo,
    e o manual interativo do Python é exibido.
    O sistema encerra quando o usuário digitar 'FIM'.
    """

    # Códigos de cores ANSI
    COR_TITULO = '\033[44m'   # fundo azul
    COR_TEXTO = '\033[7m'    # invertido
    COR_FIM = '\033[m'       # reset

    while True:
        print(f'{COR_TITULO}{" SISTEMA DE AJUDA PYTHON ":^40}{COR_FIM}')
        comando = str(input('Função ou biblioteca > ')).strip()

        if comando.upper() == 'FIM':
            print(f'{COR_TITULO}{" ATÉ LOGO! ":^40}{COR_FIM}')
            break

        print(f'{COR_TEXTO}')
        help(comando)
        print(f'{COR_FIM}')


# Programa principal
ajuda()

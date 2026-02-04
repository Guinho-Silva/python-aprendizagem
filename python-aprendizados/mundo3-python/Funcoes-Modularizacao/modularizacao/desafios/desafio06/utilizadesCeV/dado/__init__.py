def leiaMoney(msg):
    valido = False
    while not valido:

        valor = str(input(msg)).replace('.', ',')
        if valor.isalpha() or valor.strip() == '':
            print('\033[31m\"{valor}\" é um preço inválido!\033[m')
        else:   
            valido = True 
            return float(valor)   

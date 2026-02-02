def leiaMoney(p):
    
    while True:

        valor = input(p).strip()
        if valor.isnumeric():
            return float(valor)      
        else:    
          print('\033[31mNúmero inválido!\033[m')
    

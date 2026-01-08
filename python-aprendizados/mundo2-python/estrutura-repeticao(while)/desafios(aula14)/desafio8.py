
num = int(input('Digite um valor: '))

quantidade = 0

soma = 0


while num != 999:
    
    quantidade = quantidade + 1
    soma = soma + num 
    
    num = int(input('Digite um valor: '))

print('Você acertou em total de {} quantidade e a soma desses valores é de {}'.format(quantidade, soma))
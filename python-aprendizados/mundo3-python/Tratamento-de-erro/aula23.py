# Aula 23 - Tratamento de Erros e exceções
'''try:
    a = int(input('numerador:'))

    b = int(input('denominador:'))

    r = a / b

except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r}')

finally:
    print('Volte sempre! Muito obrigado')
'''

try:
    a = int(input('numerador:'))

    b = int(input('denominador:'))

    r = a / b

except (ValueError, TypeError):
    print(f'Tivemos um problema com os dados digitados')

except ZeroDivisionError:
    print('Não é possivel dividir um número por 0')

except KeyboardInterrupt:
    print('Nenhum dado informado')

except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')
    
else:
    print(f'O resultado é {r}')

finally:
    print('Volte sempre! Muito obrigado')
num = int(input('Digite um valor: '))


ValorMax = 0

ValorMin = 0

quantidade = 0

while num != 999:
    quantidade += 1
    media = quantidade / quantidade
    ValorMax = max(quantidade)
    ValorMin = min(quantidade)

    num = int(input('Digite um valor: '))
print('A média de todos os valores é de {} e o maior valor digitado foi {} e o menor é {}'.format(media,ValorMax, ValorMin))

'errado esse exercício!!!!!!!!!!!!!!'
'''from math import factorial
num = int(input('Digite um valor: '))

f = factorial(num)

print('O fatorial de {} é {}')

'''

num = int(input('Digite um valor: '))


fat = 1

while num > 1:
    fat *= num
    num -= 1

print(fat)

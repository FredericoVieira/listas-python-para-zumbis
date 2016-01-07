# -*- coding: utf-8 -*-

num1 = int(raw_input('Digite o valor do primeiro inteiro: '))
num2 = int(raw_input('Digite o valor do segundo inteiro: '))
num3 = int(raw_input('Digite o valor do terceiro inteiro: '))

list = [num1, num2, num3]
num_max = max(list)
num_min = min(list)

print('O maior número entre %d, %d, %d é %d') % (num1, num2, num3, num_max)
print('O menor número entre %d, %d, %d é %d') % (num1, num2, num3, num_min)
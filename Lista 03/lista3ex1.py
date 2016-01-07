# -*- coding: utf-8 -*-

num = int(raw_input('Digite o valor de um número inteiro: '))

while not (num >= 0 and num <= 10):
  print 'Número deve estar entre 0 e 10.'
  num = int(raw_input('Digite o valor do primeiro inteiro: '))

print 'Número válido!', num, 'está entre 0 e 10.'
# -*- coding: utf-8 -*-

def fibonacciRecursivo(num):
	if (num == 1 or num == 2):
  		return 1
 	return fibonacciRecursivo(num - 1) + fibonacciRecursivo(num - 2)

num = int(raw_input('Digite o valor de um número inteiro para cálculo do Fibonacci: '))
print fibonacciRecursivo(num)
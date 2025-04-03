# AULA 2C - O usuário deve informar 2 numeros e o programa deve exibir a soma, subtração, multiplicação, divisão
from COMUNS import *

exibir_header('2C')

in_numero_1_str = input('INFORME O PRIMEIRO NÚMERO: ')
in_numero_2_str = input('INFORME O SEGUNDO NÚMERO: ')

while in_numero_1_str == '' or in_numero_2_str == '':
  print('\nERRO! Informe dois números, por favor.')
  in_numero_1_str = input('\nINFORME O PRIMEIRO NÚMERO: ')
  in_numero_2_str = input('INFORME O SEGUNDO NÚMERO: ')

in_numero_1 = int(in_numero_1_str)
in_numero_2 = int(in_numero_2_str)

proc_numeros_soma = in_numero_1 + in_numero_2
proc_numeros_subtracao = in_numero_1 - in_numero_2
proc_numeros_multiplicacao = in_numero_1 * in_numero_2
proc_numeros_divisao = in_numero_1 / in_numero_2

print('\n')
print(f'{in_numero_1} + {in_numero_2} = {proc_numeros_soma}')
print(f'{in_numero_1} - {in_numero_2} = {proc_numeros_subtracao}')
print(f'{in_numero_1} x {in_numero_2} = {proc_numeros_multiplicacao}')
print(f'{in_numero_1} / {in_numero_2} = {proc_numeros_divisao:.2f}')

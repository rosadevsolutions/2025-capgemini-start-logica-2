#Divisão e resto - Solicitar 2 números

from COMUNS import *

exibir_header('2B')

in_numero_1_str = input('INFORME O PRIMEIRO NÚMERO: ')
in_numero_2_str = input('INFORME O SEGUNDO NÚMERO: ')

while in_numero_1_str == '' or in_numero_2_str == '':
  print('\nERRO! Informe dois números, por favor.')
  in_numero_1_str = input('INFORME O PRIMEIRO NÚMERO: ')
  in_numero_2_str = input('INFORME O SEGUNDO NÚMERO: ')

in_numero_1 = int(in_numero_1_str)
in_numero_2 = int(in_numero_2_str)

proc_numeros_divisao = in_numero_1/in_numero_2
proc_numeros_resto = proc_numeros_divisao % 2 == 0
proc_numero_status = 'Ímpar'

if proc_numeros_resto:
  proc_numero_status = 'Par'

out_mensagem = f'\n{in_numero_1_str}/{in_numero_2_str} = {proc_numeros_divisao}\nNÚMERO: {proc_numero_status}'

print(out_mensagem)

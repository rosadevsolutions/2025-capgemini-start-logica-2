#Trabalhando com tipos - Solicitar 3 palavras e concatená-las. Solicitar 3 números e somá-los. Exibir ambos 0oos resultados.

from COMUNS import *

exibir_header('2A')

print('INFORME 3 PALAVRAS E 3 NÚMEROS CONFORME SOLICITADO')

in_palavra_1 = input('\nPALAVRA 1: ')
in_palavra_2 = input('PALAVRA 2: ')
in_palavra_3 = input('PALAVRA 3: ')

while in_palavra_1 == '' or in_palavra_2 == '' or in_palavra_3 == '':
  print('\nERRO! Informe as 3 palavras, por favor.')
  in_palavra_1 = input('\nPALAVRA 1: ')
  in_palavra_2 = input('PALAVRA 2: ')
  in_palavra_3 = input('PALAVRA 3: ')

proc_palavras_concatenadas = in_palavra_1 + in_palavra_2 + in_palavra_3

in_numero_1 = input('\nNÚMERO 1: ')
in_numero_2 = input('NÚMERO 2: ')
in_numero_3 = input('NÚMERO 3: ')

while in_numero_1 == '' or in_numero_2 == '' or in_numero_3 == '':
  print('\nERRO! Informe os 3 números, por favor.')
  in_numero_1 = input('\nNÚMERO 1: ')
  in_numero_2 = input('NÚMERO 2: ')
  in_numero_3 = input('NÚMERO 3: ')

in_numero_1 = int(in_numero_1)
in_numero_2 = int(in_numero_2)
in_numero_3 = int(in_numero_3)

proc_numeros_somados =  in_numero_1 + in_numero_2 + in_numero_3
proc_numeros_somados_str = str(proc_numeros_somados)

out_mensagem = '\nPALAVRAS CONCATENADAS: ' + proc_palavras_concatenadas + '\nNÚMEROS SOMADOS: ' + proc_numeros_somados_str
print(out_mensagem)

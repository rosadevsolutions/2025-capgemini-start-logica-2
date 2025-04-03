# Criar um algoritmo que solicite ao usuário seu nome, seu sobrenome e apresente ao final o nome completo.

from COMUNS import *

exibir_header('1E')

in_nome = input("\nINFORME NOME: ")
in_sobrenome = input("INFORME SOBRENOME: ")

while in_nome == '' or in_sobrenome == '':
  out_mensagem = 'ERRO! Precisamos dos dados nome e sobrenome.'
  print(out_mensagem)
  in_nome = input("\nINFORME NOME: ")
  in_sobrenome = input("INFORME SOBRENOME: ")

proc_nome_completo = in_nome + ' ' + in_sobrenome
out_mensagem = '\nNOME COMPLETO: ' + proc_nome_completo
print(out_mensagem)

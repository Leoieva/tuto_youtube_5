
# user = input("")

# def string_lista(user):
#     lista_transformada = []
#     transformar = list(user.split())
#     for item in transformar:
#         string_em_numero = int(item)
#         lista_transformada.append(string_em_numero)
#     return lista_transformada

# funcao_chamada = string_lista(user)

# media_total = int(sum(funcao_chamada) / len(funcao_chamada))

# print(f"Lista: {funcao_chamada}")
# print(f"Maior número da lista: {max(funcao_chamada)}")
# print(f"Menor número da lista: {min(funcao_chamada)}")
# print(f"Média total da lista: {media_total}")

# EXERCICIO 1
#
# try:
#   first_num = int(input("Primeiro valor: "))
#   second_num = int(input("Segundo valor: "))
#   div = first_num / second_num
#   print(div)
# except ZeroDivisionError as zd:
#   print("Erro - Divisão por zero.\nSistema:",zd)
# except ValueError as ve:
#   print("Erro - Tipo de valor digitado incorreto.\nSistema:",ve)  

# EXERCICIO 2  
#
# def funcao_1():
#   print("Início da Função")
#   lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#   for i in range(15):
#     print(lista[i])
# print("Fim da Função")   
#
# print("Início do Programa")
# try:
#     funcao_1()
# except IndexError as ve:
#     print("Funcão Interrompida - Erro de Index.\nSistema:",ve)      
# finally:
#     print("Fim do Programa")  

# EXERCÍCIO 3
#
# dictionary = {}
#
# while True:
#
#     try:    
#         ra = input("RA: ")
#         nome = input("Nome: ")
#
#         if ra == "0":
#           break
#      
#         if ra in dictionary:
#             raise TypeError
#
#         if len(ra) == 7:
#             dictionary[ra] = nome
#             print(dictionary)
#
#         if len(ra) != 7:
#             raise ValueError   
#
#     except TypeError:
#         print("ERRO! - O RA digitado já está cadastrado.")
#
#     except ValueError:
#         print("ERRO! - O RA precisa ter 7 digitos.")             
#
# print(dictionary)        

# EXERCÍCIO 4
# 
# import funcoes
#
# try:
#     teste_fahrenheit = funcoes.converte_para_fahrenheit(27)
#     print("Teste: Conversão Celsius para Fahrenheit")
#     assert teste_fahrenheit == 80.6
#     print("Correto!")
#
# except AssertionError:
#     print("Erro!")
#
# try:
#     teste_celsius = funcoes.converte_para_celsius(32)
#     print("Teste: Conversão Fahrenheit para Celsius")
#     assert teste_celsius == 0
#     print("Correto!")
#
# except AssertionError:
#     print("Erro")

# tupla = (2, 1, 2, 3, 2, 2, 9, 2)
# item = 2

# def posicoes(tupla, item):
#     lista = []
#     for num in tupla:
#         if num == item:
#             lista.append(tupla.index(num))
#     print (lista) 

# posicoes(tupla, item)

tupla = [2, 1, 2, 3, 2, 2, 9, 2]
item = 2

for num in tupla:
  print(tupla.index(num))
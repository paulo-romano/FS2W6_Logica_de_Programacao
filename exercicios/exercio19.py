#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Ler uma lista de valores, até que o usuário digite "sair" 
(considere que não serão informados valores iguais) e escrevê-los 
em ordem crescente.
"""

lista = []

while True:
    entrada = input('Digite um valor:')
    if entrada == 'sair':
        break
    else:
        lista.append(entrada)


for posicao_atual_da_lista in range(1, len(lista)):
     valor_atual = lista[posicao_atual_da_lista]
     posicao_atual = posicao_atual_da_lista

     while posicao_atual > 0 and lista[posicao_atual - 1] > valor_atual:
         lista[posicao_atual] = lista[posicao_atual - 1]
         posicao_atual = posicao_atual - 1

     lista[posicao_atual] = valor_atual

print(lista)
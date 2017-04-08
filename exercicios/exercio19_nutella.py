#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Ler uma lista de valores, até que o usuário digite "sair" (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.
"""

lista = []

while True:
    entrada = input('Digite um valor:')
    if entrada == 'sair':
        break
    lista.append(entrada)

    lista.sort()

print(lista)
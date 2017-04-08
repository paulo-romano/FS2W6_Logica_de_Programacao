#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e
 R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o
  número de maçãs compradas, calcule e escreva o custo total da compra.
"""

quant_macas = int(input("quantida de maças "))


se_menor_12 = 1.30
se_maior_igual_12 = 1.00

if quant_macas < 12:
    custo_total = se_menor_12 * quant_macas

else:
    custo_total = se_maior_igual_12 * quant_macas

print("Custo total {:0.5f}".format(custo_total))






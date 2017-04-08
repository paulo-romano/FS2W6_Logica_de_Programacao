#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média 
final deste aluno. Considerar que a média é ponderada e que o peso das notas é 
2, 3 e 5. Fórmula para o cálculo da média final é:
 ***
     n1 * 2 + n2 * 3 + n3 * 5 / 10
 ***
 
"""

n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))

media = (n1 * 2 + n2 * 3 + n3 * 5)/10

print(media)

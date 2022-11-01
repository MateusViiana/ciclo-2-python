# -*-coding:latin1-*-
a = float(input('Digite o Primeiro Numero: '))
b = float(input('Digite o Segundo  Numero: '))
c = float(input('Digite o Terceiro Numero: '))

menor = c
if a < c and a < b:
    menor = a
if b < b and b < a:
    menor = b
print(f"O menor numero digitado foi {menor}")

#Estrutura de repetição FOR

#! vai criar um repetiçao que ira mostra apenas as vogais da palavra digitada

#todo exemplo usando o iteravel
texto = input('informe um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS: # (UPPER) deixa as letras maúculas
        print(letra, end='') #end vazio deita a sequencia na mesma linha
#!-----------------------------------------------------------!#

#* range gera um numéro aleatorio podendo ser usado dessa forma range(0, 11) onde o primeiro número é inclusivo e o segundo número é excluido e não aparece, pode adicionar um terceiro número que indicará de qunatos números deverá pular range(0, 51, 5)

#todo exemplo usando a função bult-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")

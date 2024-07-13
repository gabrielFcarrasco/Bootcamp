# Fatiamento de strings é uma tecnica utilizada para retornar substrings (parte da string original), informando o inicio (start), fim(stop) e passo(step):[start:stop, [step]].

nome = 'gabriel fernando silva carrasco'

print(nome[0]) #!fatia o caracter da string correspondente ao número

print(nome[:7]) #!não adicionado o número de start ira mostrar todos os caracteres até o stop no caso o número correspondente

print(nome[8:]) #!Não fornecendo o número de stop ele pula todos os caracteres iniciais correspondentes e mostra os demais sem interrupção

print(nome[8:16]) #! mostra oc catacteres especificos pois pula todos os caracteres antes do 8e não mostra os caracteres após o 15(ignora o 16)

print(nome[8:16:2]) #! o terceiro número informado ira dizer quantos caracters ira pular (step)

print(nome[:]) #!se não for informado nem o start nem o stop mostra toda a string normalmente

print(nome[::-1]) #! espelha a string invertendo todos os caracteres
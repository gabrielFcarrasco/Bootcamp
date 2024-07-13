#os operaadores logicos são ultilizados em conjunto de operadores de comparação

saldo = 1000
saque = 200
limite = 100
cliente_especial = True
contatos = []

#operadores de comparação
print('-----------------------')
print(saldo >= saque)#todo retorna verdadeiro
print(saque <= limite)#!retorna falso
print('-----------------------')

#operadores logicos
print('-----------------------')
print('         AND           ')
print('-----------------------')
print(saldo>=saque and saque<=limite)#?na operação AND é necessario que as duas comaprações sajam verdadeiras caso contrario retorna falso
print('-----------------------')
print('          OR           ')
print('-----------------------')
print(saldo>=saque or saque<=limite)#TODO: na operação OR é necessario apenas uma comparação verdadera para retornar verdadeiro
print('-----------------------')
print('         NOT           ')
print('-----------------------')
#!operador de negação NOT
print(not saldo > saque)#?retorna o inverso de verdadeiro
print(not contatos)#*é uma lista vazia entao retornaria falso, mas retornara seu inveso
print (not '')#?uma string vazia também retornaria falso mas retorna seu inverso
print(not 'string')#!retorna falso pois tem carcteres na string
print('-----------------------')
print('      AND e OR         ')
print('-----------------------')
print(saldo>=saque and saque<=limite or cliente_especial and saldo>=saque)
print('--------------------------------------------')
print('com parentesis para melhorar a legibilidade')
print('--------------------------------------------')
print((saldo>=saque and saque<=limite) or (cliente_especial and saldo>=saque))
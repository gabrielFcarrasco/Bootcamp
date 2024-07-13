#Adição
print(1 + 1)

#Subtração
print(10 - 2)

#Multiplicação
print(4 * 3)

#Divisão
print(12 / 5)

#Divisão Inteira (mostra apenas o valor inteiro da divisão)
print(12 // 5)

#Modúlo (mostra o resto da divisão)
print(10 % 3)

#Exponenciação
print(2 ** 3)

#Na matemática tem regras de ordens aseguir que é usada no python tambem
#Ordens para serem seguidas:
# parentesis
# expoêntes
# multiplicação e divisão (da esquerda para direita)
# adição e subtração (da esquerda para direita)#

print(10 - 5 * 2)#multiplica primeiro
print((10 - 5) * 2)#soma primeiro pon conta do parentesis

print(10 ** 2 * 2)#calcula o expoênte de 10 elevado a dois
print(10 ** (2 * 2))#multiplica (2 X 2 = 4) => 10 ** 4

print(10 / 2 * 4)#como estão no mesmo nivel de precedencia calcula o primerio que aparecer no caso divisão

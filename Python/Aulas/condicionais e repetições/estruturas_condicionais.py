
#! if simples

saldo = 2000.00
saque = float(input('qual o valor do saque R$'))

if saldo >= saque:
    print('Realizando Saque!')
if saldo < saque:
    print('Saldo insulficiente')
#* ----------------------------------------------------#

#! usando o else no lugar
if saldo >= saque:
    print('Realizando Saque!')
else:
    print('Saldo insuficiente')
#* ----------------------------------------------------#

#! elif

opcao = int(input('Informe uma opção: '))

if opcao == 1:
    valor = float(input('Informe o valor do saque R$'))

elif opcao == 2:
    print('exibindo extrato...')
else:
    print('opção invalida')

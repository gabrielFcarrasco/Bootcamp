
#! if alinhado

#* podem ser alterados de true para false para testes
conta_normal = True
conta_universitaria = False
#* podem ser alterados os valores para testes
saldo = 2000.00
saque = float(input('Digite o valor do Saque R$'))
cheque_especial = 450.00
#* --------------------------------------------------

if conta_normal:

    if saldo > saque:
        print('Saque realizado com sucesso!')
    elif (saldo + cheque_especial):
        print('Saquerealizado usando o cheque especial!')

elif conta_universitaria:

    if saldo > saque:
        print('Saque realizado com sucesso!')
    else:
        print('saldo insuficiente')

else:
    print('O sistema não reconheceu seu tipo de conta, por favor entre en contato com seu gerente.')
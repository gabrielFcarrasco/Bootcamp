
#todo Identação é uma forma de manter o codigo mais legivel e manuseavel, em python tem uma outra função, pois os blocos de codigo são identifcados onde terminam por meio da identação

def sacar(valor):
    saldo = 500

    print('----------------------------')
    print(f'Seu saldo é de R${saldo},00')
    print('----------------------------')
    if saldo >= valor:
        saldo -= valor
        print('----------------------------')
        print(f'Seu saldo é de R${saldo},00')
        print('----------------------------')
    #!fim do if   
#*Fim do bloco

sacar(int(input('informe o valor do saque: ')))
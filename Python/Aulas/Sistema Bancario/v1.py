print('''
                Bem-Vindo ao Banco GB
      
    Escolha uma opção para iniciar seu atendimento
      
''')


menu = '''
        ---------------- Menu ----------------

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair

        -------------------------------------
        Digite abaixo o número correspondente a operação 
'''

saldo = 0.00
deposito = 0.00
extrato = ''
numero_saques = 0
LIMITE_DIARIO = 3

while True:

    opcao = input(menu)

    match opcao:
        case '1':
            deposito = float(input('Informe o valor do deposito: '))
            if deposito > 0:    
                saldo = saldo + deposito
                extrato += f'\n Deposito Realizado de R${deposito} agora seu saldo é de R${saldo}'
            else:
                print('valor digitado é invalido')
            print(f'''Deposito Realizado com sucesso!
Seu saldo agora é R${saldo}
                ''')
        case '2':
            if LIMITE_DIARIO > 0:
                saque = float(input('Informe o valor do Saque: '))
                if saldo >= saque is saque <= 500:
                    saldo = saldo - saque
                    numero_saques += 1
                    LIMITE_DIARIO -= 1
                    extrato += f'\n Saque Realizado de R${saque} agora seu saldo é de R${saldo}'
                    if numero_saques < 2:
                        print(f'Você poderá realizar mais {3 - numero_saques} saques hoje!')
                    elif numero_saques == 2:
                        print('você só tem mais 1 saque diario')
                    elif numero_saques == 3:
                        print('foram feitos o número maximo de saques disponiveis hoje!')
                elif saque > 500:
                    print('Operação falhou! Valor excede o limite de saque')
                elif saque < 0:
                    print('Operação falhou! Valor invalido')
                else:
                    print('Operação falhou! saque invalido por saldo insulficiente')
                
            else:
                print('Operação falhou! Limite diario Excedido')
        case '3':
            if saldo == 0:
                print(f'Seu saldo atual é R${saldo}. Realize um deposito!')
            else:
                print(extrato)
        case '0':
            print("Obrigado por usar nossos serviços!")
            break
        case _:
            print('Operação falhou! Opção invalida. Tente novamente')

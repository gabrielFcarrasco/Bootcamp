# repetição WHILE

#! usamos o while quando não sabemos quantas vezes será nescessario que o comando se repita

opcao = -1

while opcao != 0:
    opcao = int(input('Digite\n [1]Sacar \n [2]Extrato \n [0]Encerrar Sessão \n =>  '))
    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo o Extrato..')
    else:
        print('Obrigado por ultilizar nossos serviços, até logo')
#!-----------------------------------------------------!#


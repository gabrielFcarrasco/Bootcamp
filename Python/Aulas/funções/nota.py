print('BEM-ViNDO!')
print('descubra agora se passou na materiahg')

nome = input("qual seu nome:")

nota_a1 = input("qual sua nota da prova: ")
nota_a2 = input('qual sua nota total das ativides: ')

nota_a1 = float(nota_a1)
nota_a2 = float(nota_a2)

nota_final = nota_a1 + nota_a2

print(f'Sua nota final foi {nota_final}')

if (nota_final > 7):
    print('Parabéns você foi aprovado!')
else:
    print('você reprovou, estude para a prova final!')
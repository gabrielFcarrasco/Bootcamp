#Interpolação de Variaveis em Strings

nome = 'Gabriel'
idade = 24
profissao = 'Programador'
linguagem = 'Python'
#*--------------------------------------------------*#
#*                    Old style %                   *#
#*--------------------------------------------------*#
print('--------------------------------------------------')
print('Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s.' % (nome, idade, profissao, linguagem))#! usamos no meio do texto %s (para string) %d(para inteiros) %f (pontos flutuantes). Depois adicionamos uma %(ordem que aparecerá as variaveis). a dificuldade dele é sua comprexidade já que a ordem tem que ser exata a ordem que quer deixando um texto muito grande problematico
#*--------------------------------------------------*#
#*                 Método Format                    *#
#*--------------------------------------------------*#
print('--------------------------------------------------')
print('Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.' .format (nome, idade, profissao, linguagem))#! muito parecido com o outro metodo porém podendo ser mais dificil de se entender
print(' ')
print('Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.' .format (linguagem, profissao, idade, nome)) #! nesse metodo da para indicar qual a vairal usar em cada um começando por 0 as ordens
#*--------------------------------------------------*#
#*                    Metodo F                      *#
#*--------------------------------------------------*#
print('--------------------------------------------------')
print(f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.') #! o metodo mais ultilizado por ser mais facil de ler e tambem de se usar, apenas adicionado o f antes das aspas e colocar dentro de cada conchete o nome da variavel do codigo
print(' ')
PI = 3.14159
print(f'Valor de PI é: {PI:.2f}') #! Mostra apenas dois números depois da virgula
print(' ')
print(f'Valor de PI é:{PI:5.2f}') #! O número antes do ponto indica para o codigo quantos espaços quero adicinar antes da variavel (no caso cinco espaços em branco) 
print('--------------------------------------------------')
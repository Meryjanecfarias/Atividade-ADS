import math as mh 

# Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500:
soma = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        soma += i

print(soma)
# Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e mostrar:
    #A. Menor Altura;
    #B. Menor Altura;
meh = float('inf')
mah = float('-inf')

for i in range(15):
    altura = float(input(f'A altura da {i+1}ª pessoa: '))
    if altura < meh:
        meh = altura
    if altura > mah:
        mah = altura

print(f'A menor altura do grupo é {meh:.2f} m.')
print(f'A maior altura do grupo é {mah:.2f} m.')

# Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a
    #média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
       # negativos e o percentual de valores negativos e positivos.
soma = 0
q_positivos = 0
q_negativos = 0

while True:
    valor = float(input('Digite um valor (ou 0 para sair): '))
    if valor <= 0:
        break
    
    soma += valor
    
    if valor > 0:
        q_positivos += 1
    else:
        q_negativos += 1

total_valores = q_positivos + q_negativos
media = soma / total_valores

perc_positivos = q_positivos / total_valores * 100
perc_negativos = q_negativos / total_valores * 100

print(f'A média aritmética dos valores é {media:.2f}.')
print(f'{q_positivos} valores são positivos ({perc_positivos:.2f}% do total).')
print(f'{q_negativos} valores são negativos ({perc_negativos:.2f}% do total).')

# Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles
    #estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
        #terminar quando for lido um número negativo.
cont_0_25 = 0
cont_26_50 = 0
cont_51_75 = 0
cont_76_100 = 0

while True:
    num = float(input('Digite um número (ou um valor negativo para sair): '))
    if num < 0:
        break
    
    if 0 <= num <= 25:
        cont_0_25 += 1
    elif 26 <= num <= 50:
        cont_26_50 += 1
    elif 51 <= num <= 75:
        cont_51_75 += 1
    elif 76 <= num <= 100:
        cont_76_100 += 1

print(f'{cont_0_25} números estão no intervalo [0-25].')
print(f'{cont_26_50} números estão no intervalo [26-50].')
print(f'{cont_51_75} números estão no intervalo [51-75].')
print(f'{cont_76_100} números estão no intervalo [76-100].')

#  Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.
    #Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos. 
    # O número que encerrará a leitura será zero.
numeros = []
numero = int(input('Digite um número: '))
while numero != 0:
    numeros.append(numero)
    numero = int(input('Digite um número: '))

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 == 1]

media_pares = sum(pares) / len(pares) if len(pares) > 0 else 0
media_geral = sum(numeros) / len(numeros) if len(numeros) > 0 else 0

print(f'Números pares: {len(pares)}')
print(f'Números ímpares: {len(impares)}')
print(f'Média dos números pares: {media_pares:.2f}')
print(f'Média geral dos números: {media_geral:.2f}')

#  Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.
for i in range(101, 200, 2):
    print(i)
# Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e calcule a tabuada de N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 2 x N = 2N, ..., 10 x N = 10N.
N = int(input("Digite um número de 1 a 10: "))

while N < 1 or N > 10:
    N = int(input("Valor inválido! Digite um número de 1 a 10: "))

for i in range(11):
    print(f"{i} x {N} = {i*N}")
    
# Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em P.A contendo valores 10 valores.
A = float(input("Digite o valor inicial da P.A.: "))
R = float(input("Digite a razão da P.A.: "))

for i in range(10):
    print(A)
    A += R
    
# Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em P.G contendo 10 valores
A = float(input("Digite o valor inicial da P.G.: "))
R = float(input("Digite a razão da P.G.: "))

for i in range(10):
    print(A)
    A *= R
# Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
A = int(input("Digite um número inteiro para calcular o seu fatorial, painhooo =   "))

fatorial = 1

print(f"{A}! = ", end="")

for i in range(A, 0, -1):
    fatorial *= i
    print(i, end="")
    if i != 1:
        print(" X ", end="")
    else:
        print(" = ", end="")
        
print(fatorial)



#1001
a = int(input('Insira seu valor A aqui = '))
b = int(input('Insira seu valor B aqui = '))
x = a + b
print("X = {}".format(x))

#1002
raio = float(input('Insira o Valor do seu Raio = '))

pi = 3.14159
area = pi * (raio ** 2)

print(f"A={area:.4f}")

#1003

A = int(input('Insira seu Valor de A aqui = '))
B = int(input('Insira seu Valorzin de B aqui = '))

SOMA = A + B

print("SOMA =", SOMA)

#1004

a = int(input('Insira seu Valor de A aqui = '))
b = int(input('Insira seu Valorzin de B aqui = '))

prod = a * b

print("PROD =", prod)

#1005

A = float(input('Insira aqui seu valor de A = '))
B = float(input('Insira aqui seu valor de B - '))

media = (A * 3.5 + B * 7.5) / 11

print(f"MEDIA = {media:.5f}")

#1006
# leitura das notas:

a = float(input('Digite aqui sua 1º nota = '))
b = float(input('Digite aqui sua 2º nota = '))
c = float(input('Digite aqui sua 3º nota = '))

# cálculo da média ponderada
media = (a*2 + b*3 + c*5)/10

# exibição do resultado com 1 casa decimal
print("MEDIA = {:.1f}".format(media))

#1007

a, b, c, d = map(int, input('Insira aqui os seus valores = ').split())
diferencas = (a * b - c * d)
print("DIFERENÇA =", diferencas)

#1008

numero = int(input(' Qual o valor correspondente ao funcionário? = '))
horas = int(input('Quantas horas trabalhadas você tem? '))
valor_hora = float(input('Quanto vale sua hora trabalhada? '))

salario = horas * valor_hora

print("NUMBER =", numero)
print("SALARY = $", "{:.2f}".format(salario))

#1009

nome = input('Qual o seu nome? ')
salario_fixo = float(input('Quanto você recebe mensalmente? '))
vendas = float(input('Quanto você lucrou com suas vendas esse mês? = '))

comissao = vendas * 0.15
salario_final = salario_fixo + comissao

print(f"TOTAL = R$ {salario_final:.2f}")

#1010
# leitura dos dados da peça 1
cod_peca1, qtd_peca1, preco_peca1 = input('Valores peça 1 = ').split()
cod_peca1 = int(cod_peca1)
qtd_peca1 = int(qtd_peca1)
preco_peca1 = float(preco_peca1)

# leitura dos dados da peça 2
cod_peca2, qtd_peca2, preco_peca2 = input('Valores peça 2 = ').split()
cod_peca2 = int(cod_peca2)
qtd_peca2 = int(qtd_peca2)
preco_peca2 = float(preco_peca2)

# cálculo do valor total da compra
total = qtd_peca1 * preco_peca1 + qtd_peca2 * preco_peca2

# SAÍDA
print("VALOR A PAGAR: R$ {:.2f}".format(total))

#1011

raio = float(input('Digite aqui o valor do seu raio = '))
pi = 3.14159
volume = (4/3) * pi * raio**3

print("VOLUME = {:.3f}".format(volume))

#1012
# Leitura dos valores de entrada:
a, b, c = map(float, input('Insira aqui seus respectivos valores de entrada A, B e C = ').split())

# Cálculo das áreas:
    #LEMBRETE ------->
        #a) a área do triângulo retângulo que tem A por base e C por altura.
        #b) a área do círculo de raio C. (pi = 3.14159)
        #c) a área do trapézio que tem A e B por bases e C por altura.
        #d) a área do quadrado que tem lado B.
        #e) a área do retângulo que tem lados A e B.
#Cálculo:
triangulo = (a * c) / 2
circulo = mh.pi * (c ** 2)
trapezio = ((a + b) * c) / 2
quadrado = b ** 2
retangulo = a * b

# Impressão dos resultados das Formas:
print("TRIANGULO: {:.3f}".format(triangulo))
print("CIRCULO: {:.3f}".format(circulo))
print("TRAPEZIO: {:.3f}".format(trapezio))
print("QUADRADO: {:.3f}".format(quadrado))
print("RETANGULO: {:.3f}".format(retangulo))

#1013

a, b, c = input('Insira seus Valores para cálculo =  ').split() # Leitura dos Valores como str
a, b, c = int(a), int(b), int(c) # Conversão de str 

maior_ab = (a + b + abs(a - b)) / 2 # Calculo do Maior valor 
maior_abc = (maior_ab + c + abs(maior_ab - c)) / 2 #Calculo do Maior Valor entre o antecessor e o valor de C

print(f"{maior_abc} EH o maior") #Saída

#1014:

# Leitura eos valores de distância e combustível
dist = int(input('Qual a distância que será percorrida? = '))
comb = float(input('Quanto você gastou de Gasolina nesse trajeto? = '))

# Calc o consumo médio
consumo_medio = dist / comb

# Mostra o resultado com 3 casas decimais
print('{:.3f} km/l'.format(consumo_medio))

#1015:
    # LEMBRETE
    # Distancia = SQRT (X2 -X1)**2 + (Y2 - Y1)**2

x1, y1 = map(float, input('Insira seus eixos primários = ').split())
x2, y2 = map(float, input('Insira seus exios secundários = ').split())

distancia = mh.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print('{:.4f}'.format(distancia))



#1038
codigo, quantidade = map(int, input('Insira aqui o que você deseja adquirir 1.Cachorro Quente - 2.X-Salada -  3.X-Bacon - 4.Torrada 5.Refrigerante ').split())

if codigo == 1:
    preco = 4.00
elif codigo == 2:
    preco = 4.50
elif codigo == 3:
    preco = 5.00
elif codigo == 4:
    preco = 2.00
elif codigo == 5:
    preco = 1.50

total = preco * quantidade

print("Total: R$ {:.2f}".format(total))

#1040
#Valores:
n1, n2, n3, n4 = map(float, input('Insira suas notas = ').split())

#Média Ponderada:
mp = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

if mp >= 7.0:
    print(f"Media: {mp:.1f}\nAluno aprovado.")
elif mp < 5.0:
    print(f"Media: {mp:.1f}\nAluno reprovado.")
else:
    print(f"Media: {mp:.1f}\nAluno em exame.")
    exame = float(input())
    nova_media = (mp + exame) / 2
    print(f"Nota do exame: {exame:.1f}")
    if nova_media >= 5.0:
        print(f"Aluno aprovado.\nMedia final: {nova_media:.1f}")
    else:
        print(f"Aluno reprovado.\nMedia final: {nova_media:.1f}")
        
#1041
x, y = map(float, input('Insira X e Y = ').split())

if x == y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
else:
    print("Q4")

#1043
# Lê os valores de A, B e C
a, b, c = map(float, input('Insira os valores de A, B e C por favor = ').split())

# Condição de  Verificação se os valores formam um triângulo:
if a + b > c and a + c > b and b + c > a:
    
    # Calcula o perímetro
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    # Calcula a área do trapézio
    area = (a + b) * c / 2
    print(f"Area = {area:.1f}")
    
#1044
a, b = map(int, input().split())

if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
    
#1048
salario = float(input('Digite aqui o valor do seu salário = '))

if salario <= 400:
    percentual = 15
elif salario <= 800:
    percentual = 12
elif salario <= 1200:
    percentual = 10
elif salario <= 2000:
    percentual = 7
else:
    percentual = 4

reajuste = salario * percentual / 100
novo_salario = salario + reajuste

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")

#1051
salario = float(input('Qual o seu salário? = '))

if salario <= 2000.00:
    print("Isento")
else:
    if salario <= 3000.00:
        imposto = (salario - 2000.00) * 0.08
    elif salario <= 4500.00:
        imposto = (1000.00 * 0.08) + ((salario - 3000.00) * 0.18)
    else:
        imposto = (1000.00 * 0.08) + (1500.00 * 0.18) + ((salario - 4500.00) * 0.28)

    print("R$ {:.2f}".format(imposto))
    
#1059 - 
for i in range(2, 101, 2):
    print(i)
    
#1067
#Impressão
X = int(input('Digite aqui seu valor inteiro = '))
#Saída
for i in range(1, X+1, 2):
    print(i)
    

#Faça um Programa que leia cinco números inteiros e mostre o maior e o menor deles.
'''menor = float('inf')
maior = float('-inf')

for x in range (5):
 numero = int(input(f'digite o numero {x + 1} aqui: '))
  
 if numero > maior:
  maior = numero

 if numero < menor:
   menor = numero

print("o maior numero é: ", + maior)
print('o menor numero é: ', + menor)'''

#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M = Manhã ou T = Tarde ou N- Noite. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""turno = str(input('digite o turno que você estuda: M(manhã), T(tarde) e N(noturno) '))
manhã = str('m')
tarde = str('t')
noite = str('n')

if turno.lower() in manhã:
  print("Bom dia!!")
elif turno.lower() in tarde:
  print('boa tarde')
elif turno.lower() in noite:
  print('boa noite')
else:
  print(' valor invalido')"""

#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
"""l1 = float(input("Digite o primeiro lado do triangulo; "))
l2 = float(input("Digite o segundo lado do triangulo: "))
l3 = float(input("Digite o terceiro lado do triangulo: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
      print("equilátero")
    elif l1 == l2 or l2 == l3 or l3 == l1:
      print("isosceles")
    elif l1 != l2 != l3:
      print("escaleno")
else:
   print("não é um triangulo")"""

#Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do numero. Se o número for negativo, mostre uma mensagem dizendo que o número e inválido.

"""numero = float(input("digite seu numero aqui: "))

if numero >= 0:
  raiz = numero**0.5
  print(f"a raiz quadrada do {numero} é {raiz:.2f}")
elif numero < 0:
  print('numero invalido')"""

#Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto e, domingo = 1, segunda-feira = 2, e assim por diante.
"""numero = int(input("digite seu numero de 1 a 7: "))

if numero == 1:
  print("domingo = ", + numero)
elif numero == 2:
  print(f"segunda-feira = {numero}")
elif numero == 3: 
  print(f"terça-feira = {numero}")
elif numero == 4:
  print(f"quarta-feira = {numero}")
elif numero == 5:
  print(f"quinta-feira = {numero}")
elif numero == 6:
  print(f"sexta-feira = {numero}")
elif numero == 7:
  print(f"sabado = {numero}")
else:
  print("numero inválido")"""

#Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida.
#Escolha a opção:
#1- Soma de 2 números.
#2- Difereça entre 2 números (maior pelo menor).
#3- Produto entre 2 números.
#4- Divisão entre 2 números (o denominador não pode ser zero)

"""num1 = float(input("Escreva o primeiro número: "))
num2 = float(input("Escreva o segundo número: "))
operação = str(input("qual operação que você deja fazer? a) SOMAR b) SUBTRAÇÃO c) MULTIPLICAR d) DIVISÃO:   "))

if (operação.lower() == "somar" or operação.lower() == "a"):
  print(num1 + num2)
elif (operação.lower() == "subtração" or operação.lower() == "b"):
 print(num1 - num2)
elif (operação.lower() == "multiplicar"  or operação.lower() == "c"):
 print (num1 * num2)
elif(operação.lower() == "divisão" or operação.lower() =="d"):
  if num2 !=0:
   print(num1/num2)
else:
  print("essa opção é inválida!!!")"""
#Leia o salario de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima:
#Empréstimo não concedido.

#Caso contrario, imprima:

#Empréstimo concedido

"""salario = float(input("qual é seu salario bruto? "))
empréstimo = float(input("quanto que você quer pegar emprestado? "))
parcelas = int(input("quantas parcelas voce vai pagar? "))
prestação = empréstimo/parcelas
print(f"O valor de cada parcela é:{prestação}")

if prestação > 0.2 * salario:
  print("EMPRÉSTIMO NÃO CONCEDIDO!")
else:
  print("empréstimo concedido!")"""

#Escreva um programa que leia um numero inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos. Por exemplo, ao numero 251 corresponder ao valor 8 (2 + 5 + 1). Se o numero lido não for maior do que zero, o programa terminará com a mensagem “Numero inválido”

"""numero = input("digite o número: ")
soma = sum(int(digito) for digito in numero)
if soma >= 0:
 print(f"a soma dos algoritmos é:   {soma}")
elif soma < 0:
  print("numero inválido ")"""


#Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são:
#• Ter pelo menos 65 anos,

#• Ou ter trabalhado pelo menos 30 anos,

#• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

'''idade = int(input("digite a sua idade atual: "))

temp_trabalho = int(input("digite seu tempo de trabalho: "))

if idade >= 65 or temp_trabalho>=30 or (idade >= 60 and temp_trabalho ==25):
  print("voce pode se aposentar!")
else:
  print("você não pode se aposentar ")'''

#Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado em que ele sera vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.

valor = float(input("qual valor que você esta disposto a pagar por esse produto? "))
print("Lembrando que tem uma taxa para cada região.")
taxa = str(input("Qual estado em que você gostaria de receber o produto? ")).strip()
mg = valor * 0.07
sp = valor * 0.12
rj = valor * 0.15
ms = valor * 0.08

if (taxa.lower() == "minas gerais" or taxa.lower() == "mg"):
  print("preço com taxa + valor: ", mg + valor, "R$")
elif (taxa.lower() == "são paulo" or taxa.lower() == "sp"):
  print("preço com taxa + valor: ", sp + valor, "R$")
elif (taxa.lower() == "rio de janeiro" or taxa.lower() == "rj"):
  print("preço com taxa + valor: ", rj + valor, "R$")
elif (taxa.lower() == "mato grosso do sul" or taxa.lower() == "ms"):
  print("preço com taxa + valor: ", ms + valor, "R$")
else:
  print("ERRO!!!")



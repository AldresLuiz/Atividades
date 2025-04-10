# https://github.com/AldresLuiz/Atividades

cont=0
def marcador():
    global cont
    cont += 1
    print("\n","-"*40," Atividade(",cont,")\n")

print("\n","-"*40," Operadores Matemáticos (1-10)")

marcador()
# 1. Escreva um programa que some dois números inteiros e exiba o resultado

A = 10
B = 20

print("A = ",A,", B = ",B,", A soma de A e B é",A+B)

marcador()
# 2. Crie um programa que leia dois números e exiba a subtração entre eles

C = int(input("Insira Um Número Inteiro a Variavel 'C': "))
D = int(input("Insira Um Número Inteiro a Variavel 'D': "))

print("A Subtração de 'C-D' é ",C-D)

marcador()
# 3. Faça um programa que multiplique dois números reais (float)

F = 1.77
G = 4.9

print("A Resultado Da Multiplicação Entre Numeros Reais 'F*G' é ",F*G)

marcador()
# 4. Crie um programa que divida dois números e mostre o quociente

exerc04_bool = True

def exercicio4():
    H = int(input("Insira Um Número Inteiro Diferente de 0: "))
    I = int(input("Insira Um Número Inteiro Diferente de 0: "))

    if H==0 or I==0:
        print("Erro! Não é possivel dividir por 0\n")
        return None
    
    return H/I

while exerc04_bool:
    exerc04_float = exercicio4()

    if exerc04_float != None:
        exerc04_bool = False


print("O Resultado Da Divisão é ",exerc04_float)

marcador()
# 5. Escreva um programa que calcule o resto da divisão entre dois números.

exerc05_bool = True

def exercicio5():
    J = int(input("Insira um número inteiro diferente de 0: "))
    K = int(input("Insira um número inteiro diferente de 0: "))

    if J==0 or K==0:
        print("ERRO! Não é possivel dividir por 0\n")
        return None
    
    return J%K

while exerc05_bool:
    exerc05_int = exercicio5()

    if exerc05_int != None:
        exerc05_bool = False

print("O resto da divisão é ",exerc05_int)

marcador()
# 6. Calcule a média aritimética entre três número reais

L = 5.9
M = 9.4
N = 7.2

print("A Média entre 'L','M','N' é ",(L+M+N)/3)

marcador()
# 7. Faça um programa que eleve um número ao quadrado

O = int(input("Insira um número inteiro: "))

print(O,"ao quadrado é",O**2)

marcador()
# 8. Leia dois números e calcule o quadrado da soma deles

P = int(input("Insira um número inteiro: "))
Q = int(input("Insira um número inteiro: "))

print(P,"+",Q,"ao quadrado é",(P+Q)**2)

marcador()
# 9. Escreva um programa que leia a base e a altura de um triângulo e calcule sua área

R = float(input("Qual o tamanho da base do triângulo: "))
S = float(input("Qual o tamanho da altura do triângulo: "))

print("A base do triangulo é",R,"a altura",S,"e a área é",(R*S)/2)

marcador()
# 10. Calcule o valor final de um produto com desconto de 10%

T = float(input("Insira um valor de produto: "))

print("O preço do produto com 10% de desconto é",T*0.90)

print("/n","-"*40," Operadores Lógicos e Comparativos (11-20)")

marcador()
# 11. Leia dois números e verifique se o primeiro é maior que o segundo

U = int(input("Insira o primeiro número: "))
V = int(input("Insira o segundo número: "))

print("O primeiro número é maior que o segundo?", U > V)

marcador()
# 12. Verifique se um número é positivo e par

W = int(input("Insira um número: "))

print("O número é positivo?", W > 0)
print("O número é par?", W % 2 == 0)

marcador()
# 13. Verifique se a idade informada está entre 18 e 60 anos

idade = int(input("Insira sua idade: "))

print("A idade está entre 18 e 60 anos?", 18 <= idade <= 60)

marcador()
# 14. Crie um programa que diga se um número é múltiplo de 3 ou de 5

X = int(input("Insira um número: "))

print("O número é múltiplo de 3 ou de 5?", X % 3 == 0 or X % 5 == 0)

marcador()
# 15. Peça ao usuário um valor e diga se ele não é igual a zero

Y = int(input("Insira um valor: "))

print("O valor não é igual a zero?", Y != 0)

marcador()
# 16. Verifique se um número está fora do intervalo de 0 a 100

Z = int(input("Insira um número: "))

print("O número está fora do intervalo de 0 a 100?", Z < 0 or Z > 100)

marcador()
# 17. Leia duas senhas e verifique se são iguais

senha1 = input("Insira a primeira senha: ")
senha2 = input("Insira a segunda senha: ")

print("As senhas são iguais?", senha1 == senha2)

marcador()
# 18. Pergunte se uma pessoa tem mais de 18 anos e se tem CNH; diga se pode dirigir

idade = int(input("Qual a sua idade? "))
tem_cnh = input("Você tem CNH? (sim/não): ").strip().lower() == "sim"

print("Pode dirigir?", idade >= 18 and tem_cnh)

marcador()
# 19. Leia duas strings e verifique se são diferentes

string1 = input("Insira a primeira string: ")
string2 = input("Insira a segunda string: ")

print("As strings são diferentes?", string1 != string2)

marcador()
# 20. Verifique se um número é menor que 10 ou maior que 50

numero = int(input("Insira um número: "))

print("O número é menor que 10 ou maior que 50?", numero < 10 or numero > 50)

print("\n", "-" * 40, " Tipos de Dados (int, float, bool, str) (21-30)")

marcador()
# 21. Crie uma variável do tipo int, float, bool e str, e exiba seus tipos

var_int = 10
var_float = 10.5
var_bool = True
var_str = "Olá"

print("Tipos: int:", type(var_int), ", float:", type(var_float), ", bool:", type(var_bool), ", str:", type(var_str))

marcador()
# 22. Leia um número como str e converta para int

num_str = input("Insira um número como string: ")
num_int = int(num_str)

print("Número convertido para int:", num_int)

marcador()
# 23. Leia um número decimal como str e converta para float

num_decimal_str = input("Insira um número decimal como string: ")
num_float = float(num_decimal_str)

print("Número convertido para float:", num_float)

marcador()
# 24. Converta um valor lógico True para string e imprima

bool_value = True
bool_str = str(bool_value)

print("Valor lógico convertido para string:", bool_str)

marcador()
# 25. Crie um programa que receba o nome, idade e altura e exiba formatado

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
altura = float(input("Insira sua altura (em metros): "))

print(f"Nome: {nome}, Idade: {idade} anos, Altura: {altura:.2f} metros")

marcador()
# 26. Leia um número e exiba quantas casas decimais ele tem

numero = input("Insira um número decimal: ")
casas_decimais = len(numero.split(".")[1]) if "." in numero else 0

print("O número possui", casas_decimais, "casas decimais")

marcador()
# 27. Leia uma string e diga quantos caracteres ela possui

string = input("Insira uma string: ")

print("A string possui", len(string), "caracteres")

marcador()
# 28. Leia um número inteiro e converta-o para float

num_inteiro = int(input("Insira um número inteiro: "))
num_convertido = float(num_inteiro)

print("Número convertido para float:", num_convertido)

marcador()
# 29. Faça um programa que leia dois valores booleanos e aplique and entre eles

bool1 = input("Insira o primeiro valor booleano (True/False): ").strip().capitalize() == "True"
bool2 = input("Insira o segundo valor booleano (True/False): ").strip().capitalize() == "True"

print("Resultado do AND entre os valores:", bool1 and bool2)

marcador()
# 30. Peça ao usuário dois números e diga se suas somas como int e float são iguais

num1 = input("Insira o primeiro número: ")
num2 = input("Insira o segundo número: ")
soma_int = int(float(num1)) + int(float(num2))
soma_float = float(num1) + float(num2)

print("As somas como int e float são iguais?", soma_int == soma_float)




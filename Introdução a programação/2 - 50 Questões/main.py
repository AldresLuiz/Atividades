# https://github.com/AldresLuiz/Atividades

cont=0
def marcador():
    global cont
    cont += 1
    print("\n","-"*64," Atividade(",cont,")\n")

print("\nOperadores Matemáticos (1-10)")

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
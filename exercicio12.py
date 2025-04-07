multiplicacao = 0
num = int(input("Digite um número inteiro de 1 a 10 para receber a sua tabuada: "))

for j in range (1, 11):
    multiplicacao = num*j
    print(f"{j} X {num} = {multiplicacao}")
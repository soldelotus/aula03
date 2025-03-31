#Dados de entrada
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
porcentagem = float(input("Digite, em números, qual a porcentagem de aumento você recebeu: "))
#Cálculos
aumento = (salario/100) * porcentagem
novosalario = aumento + salario
#Saídas
print(f"O seu nome é {nome}, você tem {idade} anos e recebia um salário de R${salario}")
print(f"O seu novo salário, após os {porcentagem}% de aumento, ou seja, {aumento} reais, é de R${novosalario}")
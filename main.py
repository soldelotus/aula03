nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
porcentagem = int(input("Digite, em números, qual a porcentagem de aumento você recebeu: "))

# salario / 100 x porcento

aumento = (salario/100) * porcentagem
novosalario = aumento + salario

print(f"O seu nome é {nome}, você tem {idade} anos e recebia um salário de R${salario}")
print(f"O seu novo salário, após os {porcentagem}% de aumento, é de R${novosalario}")
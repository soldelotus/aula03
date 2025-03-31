aluno = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if media >= 7.0 :
    print(f"A média foi {media:.2f} e {aluno} foi aprovado(a)!")
elif (media >= 4):
    print(f"A média foi {media:.2f} e {aluno} foi para recuperação.")
else:
    print(f"A média foi {media:.2f} e {aluno} foi para reprovado.")
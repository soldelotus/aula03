aluno = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if media >= 7.0 :
    print(f"A média foi {media} e {aluno} foi aprovado(a)!")
else:
    print(f"A média foi {media} e {aluno} foi reprovado(a).")

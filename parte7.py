time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")

gol1 = int(input(f"Diga a quantidade de gols de {time1}: "))
gol2 = int(input(f"Diga a quantidade de gols de {time2}: "))

if gol1 > gol2:
    print(f"{time1} VENCEU!")
else:
    if gol1 == gol2:
        print("Houve EMPATE.")
    else:
        print(f"{time2} VENCEU!")


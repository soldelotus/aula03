tipoCombustivel = input("Digite E se você abasteceu com etanol e digite G se você abasteceu com gasolina: ")
litros = float(input(f"Digite a quantidade de litros abastecidos: "))

vGas = 5.8
vEta = 4.9

if tipoCombustivel == "E":
    precoE = vEta * litros
    print(f"Você abasteceu {litros} litros de Etanol e o valor total é R${precoE:.2f}")


elif tipoCombustivel == "G":
    precoG = vGas * litros
    print(f"Você abasteceu {litros} litros de Gasolina e o valor total é R${precoG:.2f}")

else:
    print("Tipo de combustível inválido")


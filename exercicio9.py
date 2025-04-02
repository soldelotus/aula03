hora01 = int(input("Digite o primeiro horário "))
minuto01 = int(input("Digite os primeiros minutos"))
hora02 = int(input("Digite o segundo horário "))
minuto02 = int(input("Digite os segundos minutos"))

horatotal = (hora01) + (hora02)
minutototal = (minuto01) + (minuto02)

if horatotal > 12:
    hora12 = (horatotal) - 12
    horatotal = hora12

if horatotal > 24:
    hora24 = (horatotal) - 24
    hora24 = hora - 12
    horatotal = hora24

if horatotal > 48:
    hora48 = (horatotal) - 48
    hora48 = hora48 - 24
    hora48 = hora48 - 12
    horatotal = hora48

if minutototal >= 60 and minutototal < 120:
   minuto = (minutototal) - 60
   hora = (horatotal) + 1
   print(f"{hora}h{minuto}min")

else:
    print(f"{horatotal}h{minutototal}min")



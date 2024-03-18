dia = int(input("Informe o dia: ")) 
mes = int(input("Informe o mês: "))
if (1 <= dia <=31 and mes%2 != 0 and mes <= 12) or (1 <= dia <=30 and mes%2 == 0 and mes <= 12 and mes != 2) or (1 <= dia <=28 and mes == 2):
    print(f"Dia válido: {dia}/{mes}")
else: 
    print("Dia inválido")
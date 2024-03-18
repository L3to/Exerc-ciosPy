dia = int(input("Informe o dia: ")) 
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

if ano%400 == 0 or (ano%4 == 0 and ano%100 != 0):
    anobissexto = True
else:
    anobissexto = False
    
if (1 <= dia <=31 and mes%2 != 0 and mes <= 12) or (1 <= dia <=30 and mes%2 == 0 and mes <= 12 and mes != 2) or (1 <= dia <=28 and mes == 2) or (1 <= dia <= 29 and mes == 2 and anobissexto):
    print(f"Dia válido: {dia}/{mes}/{ano}")
else: 
    print("Dia inválido")
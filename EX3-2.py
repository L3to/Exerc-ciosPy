time1 = str(input("Quem foi o time da casa? "))
time2 = str (input("E o time adversário? "))
gols1 = int(input(f"Quantos gols o {time1} fez? "))
gols2 = int(input(f"Quantos gols o {time2} fez? "))
vencedor1 = gols1 > gols2
vencedor2 = gols2 > gols1
empate = gols1 == gols2
if vencedor1:
    print (f"{time1} ganhou!")
elif vencedor2:
    print (f"{time2} ganhou!")
elif empate:
    print("Empate!")
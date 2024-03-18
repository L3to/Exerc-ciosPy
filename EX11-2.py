media1 = 40
media2 = 80
mediaponderada = 0.4 * media1 + 0.6 * media2
aulas = 72
aaulas = 62
if aaulas >= 0.7*aulas and  mediaponderada >= 60:
    print ("Aprovado!")
elif aaulas >= 0.7*aulas and  40 <= mediaponderada <=59:
    print ("Exame!")
else:
    print ("Reprovado")
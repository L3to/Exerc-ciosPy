idade = int(input("A idade? "))
if idade >= 5 and idade <= 7:
    print ("Se enquadra em Criança")
elif idade >= 8 and idade <= 10:
    print ("Se enquadra em Juvenil")
elif idade >= 11 and idade <= 15:
    print ("Se enquadra em Adolescente")
elif idade >= 16 and idade <= 30:
    print ("Se enquadra em Adulto")
else:  
    print ("Se enquadra em Senior")


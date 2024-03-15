numero_1 = int(input("Escolha um número: "))
numero_2 = int(input("Escolha um segundo número: "))
abba = numero_2 > numero_1
abo = numero_1 > numero_2
abbe = numero_1 == numero_2
if abba:
    print("Número 2 é maior que o número 1")
elif abbe: 
    print("Empate")
elif abo:
    print("O número 1 é maior que o 2")

    
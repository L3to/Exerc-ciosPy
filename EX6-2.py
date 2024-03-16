import math
numa = int(input("Um número? "))
raiz = math.sqrt (numa)
if raiz == int(raiz):
    print(f"A raiz quadrada é {raiz:.0f}")
else:
    print ("O número não possui raiz")

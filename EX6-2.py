import math
numa = int(input("Um número? "))
raiz = math.sqrt (numa)
if raiz < 0 :
    print ("Impossível extrair")
else:
    print(f"A raiz quadrada é {raiz}")

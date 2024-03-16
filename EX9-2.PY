import math

a = float(input("Coeficiente A: "))
b = float(input("Coeficiente B: "))
c = float(input("Coeficiente C: "))
delta = b**2 + 4*a*c
raiz = math.sqrt(delta)
if delta < 0:
    print("Sem raíz real")
else:
    x1= (-b + raiz)/2*a
    x2= (-b - raiz)/2*a 

    print("As raízes são:")
    print (f"Raíz X1: {x1:.0f}")
    print (f"Raíz X2: {x2:.0f}")
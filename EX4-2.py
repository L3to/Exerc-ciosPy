diasuteis = int(input("Dias úteis? "))
horastrabalhadas = float(input("Horas trabalhadas? "))
horasnormais = diasuteis * 8
valorporhoranormal = float(input("Valor pela hora? "))
salariominimo = horastrabalhadas * valorporhoranormal
horasextras = horastrabalhadas - horasnormais
if horastrabalhadas > horasnormais:
    valorhorasextras = (valorporhoranormal + 50%valorporhoranormal)
    valorhorasextrastotal = (valorhorasextras * horasextras)
    print(f"R$ {(valorporhoranormal * horasnormais) + (valorhorasextras * horasextras)} é o salário e o ganho pelas horas extras equivale à {valorhorasextrastotal}")
elif horastrabalhadas == horasnormais:
    print(f"O salário foi de R$ {horasnormais*valorporhoranormal} e não teve nenhuma hora extra")
else: print(f"Salário baseado nas horas trabalhadas: R$ {salariominimo}")

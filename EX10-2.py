preço = float(input("Quanto o produto custa? "))
pagamento = int(input("Escolha uma forma de pagamento: \n 1. A vista em dinheiro ou cheque, recebe 10% de desconto\n 2. A vista no cartão de crédito, recebe 5% de desconto\n 3. Em duas vezes, preço normal de etiqueta sem juros\n 4. Em quatro vezes, preço normal de etiqueta mais juros de 7%\n "))
if pagamento == 1 or pagamento == "A vista em dinheiro ou cheque":
    preço = preço - 0.10*preço
    print("O produto custará R$", preço)
elif pagamento == 2 or pagamento == "A vista no cartão de crédito":
    preço = preço - 0.05*preço
    print("O produto custará R$", preço)
elif pagamento == 3 or pagamento == "Em duas vezes":
    print("O produto custará R$", preço)
elif pagamento == 4 or pagamento == "Em quatro vezes":
    preço = preço + 0.07 * preço
    print("O produto custará R$", preço)
else:
    print("Inválido")


num1 = int(input("Primeiro? "))
num2 = int(input("Segundo? "))
soma = num1 + num2
multi = num1 * num2

if num1 == 0 or num2 == 0:
    print("A soma dos números",num1, "e", num2, "é dada por", soma,",a multplicação dá", multi,",já a divisão não daria certo porque um dos operadores é igual à 0, consequentemente não é possível ter um resto")
else:
    divisao = num1/num2
    resto =  num1%num2
    print("A soma dos números",num1, "e", num2, "é dada por", soma,",a multplicação dá", multi,",já a divisão daria", divisao,"e o resto da mesma", resto)

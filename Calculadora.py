print("#Calculadora#")
print("Opcao 1. somar")
print("Opcao 2. subtrair")
print("Opcao 3. dividir")
print("Opcao 4. multiplicar")
op = int(input("Escolha a opcao:"))

if(op==1):
    a1 = int(input("Digite um valor:"))
    a2 = int(input("Digite outro valor:"))
    r = a1+a2
    print("resultado",r)

elif(op==2):
    a1 = int(input("Digite um valor:"))
    a2 = int(input("Digite outro valor:"))
    r = a1-a2
    print("resultado",r)

else:
    print("Invalido!")

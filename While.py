#coding: utf-8

conta = 0
while(conta <= 10):
    conta += 1
    print(conta)

condicao = True
while(condicao):
    print("BLOCO while() e condicao==True")
    condicao = False
    break
else:
    print("BLOCO ELSE e condicao==False")

x = 0
print("while")
while(x<10):
    print(x)
    x=x+1;
else:
    print("else")
print("fim")
